import allure
from common_functions.download_chromedriver import GetChromedriver
from source.web_source.web_factory import get_web
from run_profiles.profiles import profile
from common_functions.crypto import Crypto


def set_environment(context) -> None:
    """ set_environment function create 'env' field in 'context' object which contain all profile data for current run

        Function attributes:
            context -> object which contain all shared data for current run

        Return value -> None

    """

    environment_for_the_current_run = context.config.userdata.get('env')
    tenant_for_the_current_run = context.config.userdata.get('tenant')
    context.env = profile[environment_for_the_current_run][tenant_for_the_current_run]


def set_vendor(context) -> None:
    """ set_vendor function create 'vendor' field in 'context' object which contain all profile data for current run

            Function attributes:
                context -> object which contain all shared data for current run

            Return value -> None

        """

    if 'Vendor name 1' in context.config.userdata.get('env'):
        context.vendor = 'vendor_name_1'
    elif 'Vendor name 2' in context.config.userdata.get('env'):
        context.vendor = 'vendor_name_2'


# =================================== Before =====================================

def before_all(context) -> None:
    """ before_all function will be executed once at the beginning of our tests

        Function attributes:
            context -> object which contain all shared data for current run

        Return value -> None

    """

    set_environment(context)
    set_vendor(context)
    context.crypto = Crypto()


def before_feature(context, feature) -> None:
    """ before_feature function will print in the console the name of the executing feature

        Function attributes:
            context -> object which contain all shared data for current run
            feature -> object which contain information for current feature

        Return value -> None

    """

    print(f'Executing feature: {feature.name}')


def before_scenario(context, scenario) -> None:
    """ before_scenario function will print in the console the name of the executing scenario
        and depends on 'scenario name' will load the necessary web browser or just pass the step

        Function attributes:
            context -> object which contain all shared data for current run
            scenario -> object which contain information for current scenario

        Return value -> None

    """

    print(f'Executing scenario: {scenario.name}')

    if 'no UI' not in scenario.name:
        current_browser = context.config.userdata.get('browser')
        if current_browser.lower() == 'chrome':
            get_chromedriver = GetChromedriver()
            get_chromedriver.check_chromedriver_chrome_discrepancy()
        elif current_browser.lower() == 'firefox':
            pass
        elif current_browser.lower() == 'edge':
            pass

    if 'with Mobile view' in context.scenario.name:
        context.web = get_web(context.config.userdata.get('browser'), str(context.scenario.name).split('model:')[-1])
        context.web.open_url(context.env['UI_URL'])
        context.execution_type = 'mobile'
    elif 'no UI' in context.scenario.name:
        pass
    else:
        web = get_web(context.config.userdata.get('browser'))
        context.web = web
        context.web.open_url(context.env['UI_URL'])


def before_step(context, step) -> None:
    """ before_step function will print in the console the name of the executing step

        Function attributes:
            context -> object which contain all shared data for current run
            step -> object which contain information for current step

        Return value -> None

    """

    # print("Executing step: " + step.name)
    pass


# =================================== After =====================================


def after_feature(context, feature) -> None:
    """ after_feature function will print in the console the status and the name of completed feature

        Function attributes:
            context -> object which contain all shared data for current run
            feature -> object which contain information for current feature

        Return value -> None

    """

    print(f'{str(feature.status).capitalize()} feature: {feature.name}')


def after_scenario(context, scenario) -> None:
    """ after_scenario function will print in the console the status and the name of completed scenario
        and if we have UI test closing the browser

        Function attributes:
            context -> object which contain all shared data for current run
            scenario -> object which contain information for current scenario

        Return value -> None

    """

    print(f'{str(scenario.status).capitalize()} scenario: {scenario.name}')

    if 'no UI' not in scenario.name:
        context.web.quit_browser()


def after_step(context, step) -> None:
    """ after_step function will print in the console the status and the name of current step
            and if we have UI test closing the browser

            Function attributes:
                context -> object which contain all shared data for current run
                step -> object which contain information for current step

            Return value -> None

        """

    if step.status == "failed":
        if 'no UI' not in context.scenario.name:
            screenshot_file = context.web.take_screenshot(file_name=context.scenario.name, file_extension='png',
                                                          formatter=context.config.format[0])
            if 'allure_behave' in context.config.format[0]:
                allure.attach(body=screenshot_file, name='screenshot', attachment_type=allure.attachment_type.PNG)

            print('======================== Beginning of Browser log: ===========================')
            print('||                                                                          ||')

            logs_div_html = ''
            for log in context.web._web_driver.get_log('browser'):
                print(log)
                if log['level'] == 'SEVERE':
                    logs_div_html += '<div style="background-color:red;">'
                elif log['level'] == 'WARNING':
                    logs_div_html += '<div style="background-color:yellow;">'
                else:
                    logs_div_html += f'<div>'
                logs_div_html += f'<b>level :</b>   {log["level"]}<br><b>message :</b>   {log["message"]}</div><br><br>'
            print('||                                                                          ||')
            print('======================== End of Browser log: =================================')

            attached_body = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                            <title>Log report</title>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            </head>
                            <body>
                                {logs_div_html}
                            </body>
                            </html>
            """

            allure.attach(body=attached_body, name='Web browser logs', attachment_type=allure.attachment_type.HTML)
            context.web.close_browser()


def after_all(context) -> None:
    """ after_all function will be executed once at the end of our tests

        Function attributes:
            context -> object which contain all shared data for current run

        Return value -> None

    """
    pass
