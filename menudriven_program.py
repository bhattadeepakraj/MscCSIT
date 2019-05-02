print("\nMenu:\n Choose one of the scheduling algorithm:\n(F) FCFS \n(S)Shortest Job\n(P)Priority Based \n(R) Round Robin\n(Q)uit")
choose=input(">>> ")
choice=choose.lower()
while choice!="q":
    if choice=="f":

        bt = []
        print("Enter the number of process: ")
        n = int(input())
        print("Enter the burst time of the processes: \n")
        bt = list(map(int, input().split()))

        wt = []
        avgwt = 0
        tat = []
        avgtat = 0

        wt.insert(0, 0)
        tat.insert(0, bt[0])

        for i in range(1, len(bt)):
            wt.insert(i, wt[i - 1] + bt[i - 1])
            tat.insert(i, wt[i] + bt[i])
            avgwt += wt[i]
            avgtat += tat[i]

        avgwt = float(avgwt) / n
        avgtat = float(avgtat) / n
        print("\n")
        print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")

        for i in range(0, n):
            print(str(i) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
            print("\n")

        print("Average Waiting time is: " + str(avgwt))
        print("Average Turn Arount Time is: " + str(avgtat))

    elif choice == "r":
        def findWaitingTime(processes, n, bt, wt, quantum):
            rem_bt = [0] * n

            for i in range(n):
                rem_bt[i] = bt[i]
            t = 0

            while (1):
                done = True
                for i in range(n):
                    if (rem_bt[i] > 0):
                        done = False

                        if (rem_bt[i] > quantum):
                            t += quantum

                            rem_bt[i] -= quantum
                        else:
                            t = t + rem_bt[i]
                            wt[i] = t - bt[i]
                            rem_bt[i] = 0

                if (done == True):
                    break


        def findTurnAroundTime(processes, n, bt, wt, tat):
            for i in range(n):
                tat[i] = bt[i] + wt[i]


        def findavgTime(processes, n, bt, quantum):
            wt = [0] * n
            tat = [0] * n
            findWaitingTime(processes, n, bt, wt, quantum)
            findTurnAroundTime(processes, n, bt, wt, tat)
            print("Processes    Burst Time     Waiting",
                  "Time    Turn-Around Time")
            total_wt = 0
            total_tat = 0
            for i in range(n):
                total_wt = total_wt + wt[i]
                total_tat = total_tat + tat[i]
                print(" ", i + 1, "\t\t", bt[i],
                      "\t\t", wt[i], "\t\t", tat[i])

            print("\nAverage waiting time = %.5f " % (total_wt / n))
            print("Average turn around time = %.5f " % (total_tat / n))


        if __name__ == "__main__":
            print("Enter the number of process: ")
            n = int(input())
            proc = n;
            print("Enter the burst time of the processes: \n")
            burst_time = list(map(int, input().split()))
            print("Enter the quantum time of the processes: \n")
            quantum = int(input())
            findavgTime(proc, n, burst_time, quantum)


    elif choice=="s":
        bt = []  # bt stands for burst time
        print("Enter the number of process: ")
        n = int(input())
        processes = []
        for i in range(0, n):
            processes.insert(i, i + 1)
        print("Enter the burst time of the processes: \n")
        bt = list(map(int, input().split()))
        for i in range(0, len(bt) - 1):  # applying bubble sort to sort process according to their burst time
            for j in range(0, len(bt) - i - 1):
                if (bt[j] > bt[j + 1]):
                    temp = bt[j]
                    bt[j] = bt[j + 1]
                    bt[j + 1] = temp
                    temp = processes[j]
                    processes[j] = processes[j + 1]
                    processes[j + 1] = temp
        wt = []  # wt stands for waiting time
        avgwt = 0  # average of waiting time
        tat = []  # tat stands for turnaround time
        avgtat = 0  # average of total turnaround time
        wt.insert(0, 0)
        tat.insert(0, bt[0])
        for i in range(1, len(bt)):
            wt.insert(i, wt[i - 1] + bt[i - 1])
            tat.insert(i, wt[i] + bt[i])
            avgwt += wt[i]
            avgtat += tat[i]
        avgwt = float(avgwt) / n
        avgtat = float(avgtat) / n
        print("\n")
        print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
        for i in range(0, n):
            print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
            print("\n")
        print("Average Waiting time is: " + str(avgwt))
        print("Average Turn Arount Time is: " + str(avgtat))

    elif choice=="p":
        print("Enter the number of processess: ")
        n = int(input())
        processes = []
        for i in range(0, n):
            processes.insert(i, i + 1)

        print("\nEnter the burst time of the processes: \n")
        bt = list(map(int, input().split()))

        print("\nEnter the priority of the processes: \n")
        priority = list(map(int, input().split()))
        tat = []
        wt = []

        # Sorting processes burst time, on the basis of their priority
        for i in range(0, len(priority) - 1):
            for j in range(0, len(priority) - i - 1):
                if (priority[j] > priority[j + 1]):
                    swap = priority[j]
                    priority[j] = priority[j + 1]
                    priority[j + 1] = swap

                    swap = bt[j]
                    bt[j] = bt[j + 1]
                    bt[j + 1] = swap

                    swap = processes[j]
                    processes[j] = processes[j + 1]
                    processes[j + 1] = swap

        wt.insert(0, 0)
        tat.insert(0, bt[0])

        # Calculating of waiting time and Turn Around Time of each process
        for i in range(1, len(processes)):
            wt.insert(i, wt[i - 1] + bt[i - 1])
            tat.insert(i, wt[i] + bt[i])

        # calculating average waiting time and average turn around time
        avgtat = 0
        avgwt = 0
        for i in range(0, len(processes)):
            avgwt = avgwt + wt[i]
            avgtat = avgtat + tat[i]
        avgwt = float(avgwt) / n
        avgtat = float(avgtat) / n
        print("\n")
        print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
        for i in range(0, n):
            print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
            print("\n")
        print("Average Waiting time is: " + str(avgwt))
        print("Average Turn Around Time is: " + str(avgtat))
    else:
        print("Invalid choice, please choose again")
        print("\n")