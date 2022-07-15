import time
import random
sen = ["A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing.", 
       "Hunt and peck (two-fingered typing), also known as Eagle Finger, is a common form of typing in which the typist presses each key individually.", 
       "Jim and Anne will be in charge of the spring field day to be held in early June. They will ask their friends' aid to get set up.", 
       "The fastest typing speed ever, 216 words per minute, was achieved by Stella Pajunas-Garnand from Chicago in 1946 in one minute on an IBM electric.", 
       "Proofreader applicants are tested primarily on their spelling, speed, and skill in finding errors in the sample text."]
currentText = random.choice(sen)
print(">>", currentText)

start = time.time()
user = input(">> ")
end = time.time()
timeTaken = round(end-start)
times = min(len(currentText), len(user))
cc = 0
for i in range(times):
    if currentText[i] == user[i]:
        cc+=1
print(cc)
print("--------------------------")
print(timeTaken, "secs")
timeTaken/=60
cpm = cc/timeTaken
print("CPM:", cpm)
wpm = cpm/5
print("WPM:", wpm)
accuracy = cc/len(currentText)*100
print("Accuracy:", int(accuracy), "%")
print("--------------------------")


