from tkinter import * 
 
class Calculator:
    def __init__(self):
       
        self.current_num = ""
        self.current_op = ""

        self.root = Tk()

        self.str_history = StringVar()
        self.str_result = StringVar()


        self.add_widget("display_history", Label, textvariable = self.str_history)
        self.add_widget("display_result", Label, textvariable = self.str_result)        

        self.add_widget("bAC", Button, text = "AC", command = self.cb)
        self.add_widget("bDiv", Button, text = "/", command = self.current_op_div)
        self.add_widget("bMul", Button, text = "x", command = self.current_op_mul)
        self.add_widget("bMinus", Button, text = "-", command = self.current_op_sub)
        self.add_widget("bPlus", Button, text = "+", command = self.current_op_add)
        self.add_widget("bEq", Button, text = "=", command = self.cb)
        self.add_widget("bDot", Button, text = ".", command = self.cb)
        self.add_widget("b0", Button, text = "0", command = self.append_to_current_num_0)
        self.add_widget("b1", Button, text = "1", command = self.append_to_current_num_1)
        self.add_widget("b2", Button, text = "2", command = self.append_to_current_num_2)
        self.add_widget("b3", Button, text = "3", command = self.append_to_current_num_3)
        self.add_widget("b4", Button, text = "4", command = self.append_to_current_num_4)
        self.add_widget("b5", Button, text = "5", command = self.append_to_current_num_5)
        self.add_widget("b6", Button, text = "6", command = self.append_to_current_num_6)
        self.add_widget("b7", Button, text = "7", command = self.append_to_current_num_7)
        self.add_widget("b8", Button, text = "8", command = self.append_to_current_num_8)
        self.add_widget("b9", Button, text = "9", command = self.append_to_current_num_9)

        self.display_history.grid(row = 0, column = 0, columnspan = 4, sticky = "NSEW")
        self.display_result.grid(row = 1, column = 0, columnspan = 4, sticky = "NSEW")
        self.bAC.grid(row = 2, column = 0, columnspan = 2, sticky = "NSEW")
        self.bDiv.grid(row = 2, column = 2, sticky = "NSEW")
        self.bMul.grid(row = 2, column = 3, sticky = "NSEW")
        self.bMinus.grid(row = 3, column = 3, sticky = "NSEW")
        self.bPlus.grid(row = 4, column = 3, sticky = "NSEW")
        self.bEq.grid(row = 5, column = 3, rowspan = 2, sticky = "NSEW")
        self.bDot.grid(row = 6, column = 2, sticky = "NSEW")
        self.b0.grid(row = 6, column = 0, columnspan = 2, sticky = "NSEW")
        self.b1.grid(row = 5, column = 0, sticky = "NSEW")
        self.b2.grid(row = 5, column = 1, sticky = "NSEW")
        self.b3.grid(row = 5, column = 2, sticky = "NSEW")
        self.b4.grid(row = 4, column = 0, sticky = "NSEW")
        self.b5.grid(row = 4, column = 1, sticky = "NSEW")
        self.b6.grid(row = 4, column = 2, sticky = "NSEW")
        self.b7.grid(row = 3, column = 0, sticky = "NSEW")
        self.b8.grid(row = 3, column = 1, sticky = "NSEW")
        self.b9.grid(row = 3, column = 2, sticky = "NSEW")

        cols, rows = self.root.grid_size()
        for c in range(cols): self.root.columnconfigure(c, weight = 1)
        for r in range(rows): self.root.rowconfigure(r, weight = 1)

        self.root.mainloop()




    def add_widget(self, widget_attr_name, widgetClass, *args, **kwargs):
        self.__dict__[widget_attr_name] = widgetClass(*args, **kwargs)
        # self.__dict__[widget_attr_name].pack()

    def cb(self):
        print(self.root.grid_size())




    def append_to_current_num_0(self): self.append_to_current_num(0)
    def append_to_current_num_1(self): self.append_to_current_num(1)
    def append_to_current_num_2(self): self.append_to_current_num(2)
    def append_to_current_num_3(self): self.append_to_current_num(3)
    def append_to_current_num_4(self): self.append_to_current_num(4)
    def append_to_current_num_5(self): self.append_to_current_num(5)
    def append_to_current_num_6(self): self.append_to_current_num(6)
    def append_to_current_num_7(self): self.append_to_current_num(7)
    def append_to_current_num_8(self): self.append_to_current_num(8)
    def append_to_current_num_9(self): self.append_to_current_num(9)

    def current_op_add(self): self.update_current_op(float.__add__)
    def current_op_sub(self): self.update_current_op(float.__sub__)
    def current_op_mul(self): self.update_current_op(float.__mul__)
    def current_op_div(self): self.update_current_op(float.__truediv__)


    def append_to_current_num(self, n):
        self.current_num += str(n)
        self.str_history.set(self.current_num)
        print(self.current_num)

    def update_current_op(self, op):
        self.current_op = op
        print(self.current_op(3.0, 2.0))
        


Calculator()