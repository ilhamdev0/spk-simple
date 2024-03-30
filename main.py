import interfaces
import input
import output
import services

class App:
    def __init__(self, input: interfaces.Input, config: interfaces.Input, configoutput: interfaces.Output, csvoutput: interfaces.Output, csvtopoutput: interfaces.Output, terminaloutput: interfaces.Output):
        self.input = input
        self.config = config
        self.configoutput = configoutput
        self.csvoutput = csvoutput
        self.csvtopoutput = csvtopoutput
        self.terminaloutput = terminaloutput

        self.configservices = services.Config(self.input, self.config, self.configoutput)
        self.logicservices = services.Logic(self.input, self.config, self.csvoutput)

    def preprocess(self):
        loadinput = self.input.open()
        loadconfig = self.config.open()

        if len(loadinput) == 0:
            exit()

        if len(loadconfig) == 0:
            loadconfig = self.configservices.create()
            self.configoutput.save(loadconfig)
        
        self.configservices.verify(loadinput, loadconfig)
    
    def start(self):
        data = self.logicservices.score()
        top = self.logicservices.topscore(data, data["rank"])
        self.csvoutput.save(data)
        self.csvtopoutput.save(top)

        self.terminaloutput.show()

        

if __name__ == "__main__":
    app = App(input.CSVInput(),input.CSVConfig(),output.CSVConfigOutput(),output.CSVOutput(),output.CSVTopOutput(),output.TerminalOutput())

    app.preprocess()
    app.start()