import csv

def remove_cruft(s):
    return s[:-1]

with open('names.csv', 'r') as f:
    reader = csv.reader(f)
    my_list = [[remove_cruft(item) for item in line] for line in reader]

for i in my_list:

   #Initialization
    temp=i[0]
    title = "Odmiana wyrazu: "
    i[0] =title + temp + 'ć'

    #Name inflections in time
    time_past_singular = "Czas przeszły, l.poj: "
    time_past_plural = "Czas przeszły, l.m: "
    time_present_singular = "Czas terazniejszy, l.poj: "
    time_present_plural = "Czas terazniejszy, l.m: "
    time_future_singular = "Czas przyszły, l.poj: "
    time_future_plural = "Czas przyszły, l.m: "

    #Name Inflections for Person
    #Time Past - Singular
    i.append(time_past_singular + "Ja " + (temp+ 'łem/')+ (temp + 'łam/')+ (temp + 'łom'))
    i.append(time_past_singular + "Ty " + (temp + 'łeś/') + (temp + 'łaś/') + (temp + 'łoś'))
    i.append(time_past_singular + "On/Ona/Ono " + (temp + 'ł/') + (temp + 'ła/') + (temp + 'ło'))
    #Time Past - Plural
    i.append(time_past_plural + "My " + (temp + 'liśmy/')+ (temp + 'łśmy'))
    i.append(time_past_plural + "Wy " + (temp + 'liście/') + (temp + 'łyście'))
    i.append(time_past_plural + "Oni/One " + (temp + 'li/') + (temp + 'ły'))
    #Time Present - Singular
    i.append(time_present_singular + "Ja " + (temp[:-3] + 'uję'))
    i.append(time_present_singular + "Ty " + (temp[:-3] + 'ujesz'))
    i.append(time_present_singular + "On/Ona/Ono " + (temp[:-3] + 'uje'))
    #Time Present - Plural
    i.append(time_present_plural + "My " + (temp[:-3] + 'ujemy'))
    i.append(time_present_plural + "Wy " + (temp[:-3] + 'ujecie'))
    i.append(time_present_plural + "Oni/One " + (temp[:-3] + 'ują'))
    #Time Future - Singular
    i.append(time_future_singular + "Ja " + (temp[:-3] + 'am'))
    i.append(time_future_singular + "Ty " + (temp[:-3] + 'asz'))
    i.append(time_future_singular + "On/Ona/Ono " + (temp[:-3] + 'a'))
    #Time Future - Plural
    i.append(time_future_plural + "My " + (temp[:-3] + 'amy'))
    i.append(time_future_plural + "Wy " + (temp[:-3] + 'acie'))
    i.append(time_future_plural + "Oni/One " + (temp[:-3] + 'ają'))

print(my_list)

with open('names_inflection.csv','w') as output:
    writer = csv.writer(output)
    for val in my_list:
      writer.writerow([val])
