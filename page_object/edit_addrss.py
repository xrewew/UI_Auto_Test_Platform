from base_page.Webkey import BasePage


class EditAddrssPage(BasePage):
    #1.定义页面的URL:方便对于不同页面的对象的管理，不需要再浪费时间去记url
    url = 'http://127.0.0.1:8000/user/site/'
    #2.定义页面的核心元素:页面中的核心元素也就是需要操作的元素，除此之外其他元素与我们没有任何元素
    address_name = ('xpath','/html/body/div[3]/div[2]/div[2]/form/div[1]/input')
    address_phone = ('xpath','/html/body/div[3]/div[2]/div[2]/form/div[2]/input')
    address_email = ('xpath','/html/body/div[3]/div[2]/div[2]/form/div[3]/input')
    address_detail = ('xpath','/html/body/div[3]/div[2]/div[2]/form/div[4]/textarea')
    edit_button = ('xpath','/html/body/div[3]/div[2]/div[2]/form/input[2]')

    #3.页面的核心业务流程
    def user_edit_address(self,name=None,phone=None,email=None,detail=None):
        """
        # 给每个参数赋值None，默认值为None，原因是因为在编辑地址功能中，用户可能只需要编辑其中的某几个字段，而不是全部字段。在通过if判断时，
        # 如果参数为None，则不进行操作，保留原有的值。如果参数不为None，则进行操作，更新为新的值。
        :param name: 姓名
        :param phone: 手机号
        :param email: 邮箱
        :param detail: 详细地址
        :return:
        """
        self.open(self.url)
        if name:
            self.input(*self.address_name,txt=name)
        if phone:
            self.input(*self.address_phone,txt=phone)
        if email:
            self.input(*self.address_email,txt=email)
        if detail:
            self.input(*self.address_detail,txt=detail)
        self.click(*self.edit_button)
        self.wait(1)
