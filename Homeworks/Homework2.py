CV1 = {"Name" : "Aslı", "Lastname" : "Doğan", "Birth Date" : "22/05/1998" , "Job" : "Dentist"}
CV2 = {"Name" : "Nihat", "Lastname" : "Kaya", "Birth Date" : "12/06/1996" , "Job" : "Nurse"}
CV3 = {"Name" : "Simge", "Lastname" : "Deniz", "Birth Date" : "18/08/1997" , "Job" : "Taxi Driver"}
CV4 = {"Name" : "Rasim", "Lastname" : "Yılmaz", "Birth Date" : "22/09/2000" , "Job" : "Teacher"}
CV5 = {"Name" : "Anıl", "Lastname" : "Yıldız", "Birth Date" : "23/02/1994" , "Job" : "Organizatör"}

all_CVs = [CV1, CV2, CV3, CV4, CV5]

for i in all_CVs:
    print(i["Name"] + " " + i["Lastname"] + " " + i["Birth Date"] + " " + i["Job"])