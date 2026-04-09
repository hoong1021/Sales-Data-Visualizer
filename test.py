
from json import loads
from pyecharts.charts import Bar
from pyecharts.options import *
from abc import ABC, abstractmethod
class FileReader(ABC):
    @abstractmethod
    def read_file(self):
        pass
class TextReader(FileReader):
    def __init__(self,file:str,datas:dict):
        self.file = str(file)
        self.datas = datas
    def read_file(self) -> dict:
        with open(self.file,"r",encoding = "utf-8") as self.f:
            data = [line.strip("\n").split(",") for line in self.f.readlines()]
            for i in data:
                date = i[0]
                money = int(i[2])
                if date in self.datas:
                   self.datas[date] += money
                else:
                   self.datas[date] = money
            return self.datas
class JsonReader(FileReader):
    def __init__(self,file:str,datas:dict):
        self.file = str(file)
        self.datas = datas
    def read_file(self) -> dict:
        with open(self.file,"r",encoding = "utf-8") as self.f:
            data_json = [loads(line) for line in self.f.readlines()]    
            for i in data_json:
                money = i.get("money",0)
                date = i.get("date","X")
                if date in self.datas:
                    self.datas[date] += money
                else:
                    self.datas[date] = money
            return self.datas
txt = TextReader("data/2011年1月销售数据.txt",{})
jsonn = JsonReader("data/2011年2月销售数据JSON.txt",{})
class DataProducer:
    def __init__(self,reader:FileReader):
        self.reader = reader
    def get_data(self):
        final = self.reader.read_file()
        x = [i for i in final.keys()]
        y = [j for j in final.values()]
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("",y,label_opts = LabelOpts(position = "right"))
            .reversal_axis()
        )
        bar.render()
i = DataProducer(jsonn)
i.get_data()