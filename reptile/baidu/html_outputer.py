# coding utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        # font = open('output.html', 'w')
        for item in self.datas:
            print(item)