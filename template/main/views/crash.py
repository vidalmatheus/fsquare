from commons.utils import sleep


def break_on_purpose(request, exception=Exception('Break on purpose')):
    sleep(int(request.GET.get('sleep', '0')))
    raise exception
