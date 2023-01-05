import view
import data_base
import func


def start():
    a, znak, b = view.input_()
    data_base.write_(a, znak, b)
    list=data_base.read_().split('|')
    result=func.function(list[0],list[1],list[2])
    view.view_(result)
    
