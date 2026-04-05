import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.csv", delimiter =",", skiprows = 1)
time = data[:, 0]
temperature = data[:, 1]
humidity = data[:, 2]


while True:
    print("1.Line Graph:")
    print("2.Bar Graph:")
    print("3.Pie Chart:")
    print("4.Exit:")
    
    choice = int(input("Enter your choice:"))


    if choice == 1:
        print("Loading Line Graph: ")
        
        max_temp = max(temperature)
        min_temp = min(temperature)
        avg_temp = sum(temperature) / len(temperature)

        max_hum = max(humidity)
        min_hum = min(humidity)
        avg_hum = sum(humidity) / len(humidity)

        print("Temp -> Max:", max_temp, "Min:", min_temp, "Avg:", round(avg_temp,2))
        print("Humidity -> Max:", max_hum, "Min:", min_hum, "Avg:", round(avg_hum,2))         
        
        plt.figure()
        plt.suptitle("Weather Data Visualization", size = 15)
        
        plt.subplot(2,1,1)
        plt.plot(time, temperature, color = "skyblue", marker = "." , markersize = 8)
        plt.grid()
        plt.title("Temperature", size = 12)
        plt.xlabel("Time", size = 10)
        plt.ylabel("Value", size = 10)
        
        plt.subplot(2,1,2)
        plt.plot(time, humidity, color ="orange",marker = "." , markersize = 8)
        plt.grid()
        plt.title("Humidity", size = 12)
        plt.xlabel("Time", size = 10)
        plt.ylabel("Value", size = 10)
        
        plt.tight_layout()
        plt.show()
        
    elif choice == 2:
        print("Loading Bar Graph: ")
        
        max_temp = max(temperature)
        min_temp = min(temperature)

        max_hum = max(humidity)
        min_hum = min(humidity)

        print("Temp -> Max:", max_temp, "Min:", min_temp)
        print("Humidity -> Max:", max_hum, "Min:", min_hum)
        
        plt.figure()
        plt.suptitle("Weather Forecasting", size = 15)
        
        plt.subplot(2,1,1)
        plt.bar(time, temperature, color = "skyblue", edgecolor = "blue")
        plt.title("Temperature", size = 12)
        plt.xlabel("Time", size = 10)
        plt.ylabel("Value", size = 10)
        
        plt.subplot(2,1,2)
        plt.bar(time, humidity, color = "orange", edgecolor = "darkorange")
        plt.title("Humidity", size = 12)
        plt.xlabel("Time", size = 10)
        plt.ylabel("Value", size = 10)
        
        plt.tight_layout()
        plt.show()
        
    elif choice == 3:
        print("Loading Pie Chart: ")
        
        low_temp = 0
        mid_temp = 0
        high_temp = 0

        for t in temperature:
            if t < 25:
                low_temp += 1
            elif t < 30:
                mid_temp += 1
            else:
                high_temp += 1

        temp_counts = [low_temp, mid_temp, high_temp]

        low_hum = 0
        mid_hum = 0
        high_hum = 0

        for h in humidity:
            if h < 50:
                low_hum += 1
            elif h < 70:
                mid_hum += 1
            else:
                high_hum += 1

        hum_counts = [low_hum, mid_hum, high_hum]

        labels = ["Low", "Medium", "High"]
        
        print("Temperature Distribution:", temp_counts)
        print("Humidity Distribution:", hum_counts)
        
        plt.figure()
        plt.subplot(1,2,1)
        plt.pie(temp_counts, labels=labels, autopct = "%1.1f%%" , shadow = True,
                wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
        plt.title("Temperature", size = 12)
        
        plt.subplot(1,2,2)
        plt.pie(hum_counts,labels=labels, autopct = "%1.1f%%", shadow = True,
                wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
        plt.title("Humidity")
        
        plt.show()
        
    elif choice == 4:
        print("Exiting Program..")
        break
    
    else:
        print("Invalid choice, please try again..")
        
        
        
        
        
        
        
