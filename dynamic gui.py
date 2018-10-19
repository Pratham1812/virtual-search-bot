import wx
import wikipedia
import wolframalpha
from gtts import gTTS
import os
import webbrowser

tts = gTTS(text="Hello!!! I am Your Personal Assistant", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
        #wolframalpha
            app_id = "JKL97W-U4ALW628KV"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (answer)
            tts = gTTS(text=answer, lang='en')
            tts.save("answer.mp3")
            # to start the file from python
            os.system("answer.mp3")


            
        except:
            #wikipedia
            tts = gTTS(text="You Searched for"+input, lang='en')
            tts.save("input.mp3")
            # to start the file from python
            os.system("input.mp3")

            result = (wikipedia.summary(input))
            if result == "(data not available)":                           
                try:
                    webbrowser.open_new(input)
                    webrowser.get('Google Chrome').open_new(input)
                    webbrowser.open_new_tab(url)
                    webbrowser.get('Google Chrome').open_new_tab(input)
                except:
                    print(result)
                    
        
            


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
