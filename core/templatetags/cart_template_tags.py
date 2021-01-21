from django import template
from core.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

#模板中调用函数 得用注册的模板库register = template.Library()修饰函数
#{% load cart_template_tags %} 模板中加载脚本
#{{ request.user|cart_item_count }} 购物车数量函数 user作为参数传入