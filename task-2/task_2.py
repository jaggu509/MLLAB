import pandas as pd
import matplotlib.pyplot as plt


#Histogram
def histogram():
    df.hist()
    plt.title("Histogram")
    plt.show()


#Bar chart
def bar_chart():
    df.plot.bar()
    plt.bar(df["Age"], df["Sales"])
    plt.xlabel("Age")
    plt.ylabel("Sales")
    plt.title("Age vs Sales")
    plt.show()



#Box plot chart
def box_plot_chart():
    df.plot.box()
    plt.boxplot(df["Income"])
    plt.title("Income Box Plot Chart")
    plt.show()



#Pie Chart
def pie_chart():
    plt.pie(df["Age"], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"},
                    autopct = "%1.1f%%")
    plt.title("Age")
    plt.show()

    plt.pie(df["Income"], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"},
                    autopct = "%1.1f%%")
    plt.title("Income")
    plt.show()

    plt.pie(df["Sales"], labels = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"},
                    autopct = "%1.1f%%")
    plt.title("Sales")
    plt.show()



#Scatter plot
def scatter_plot():
    plt.scatter(df["Income"], df["Sales"])
    plt.xlabel("Income")
    plt.ylabel("Sales")
    plt.title("Scatter-1")
    plt.show()

    plt.scatter(df["Sales"], df["Age"])
    plt.xlabel("Sales")
    plt.ylabel("Age")
    plt.title("Scatter-2")
    plt.show()
    
if __name__ == "__main__":

    data = [['E001', 'M', 34, 123, 'Normal',      350],
            ['E002', 'F', 40, 114, 'Overweight',  450],
            ['E003', 'F', 37, 135, 'Obesity',     169],
            ['E004', 'M', 30, 139, 'Underweight', 189],
            ['E005', 'F', 44, 117, 'Underweight', 183],
            ['E006', 'M', 36, 121, 'Normal',       80],
            ['E007', 'M', 32, 133, 'Obesity',     166],
            ['E008', 'F', 26, 140, 'Normal',      120],
            ['E009', 'M', 32, 133, 'Normal',       75],
            ['E010', 'M', 36, 133, 'Underweight',  40] 
    ]


    df = pd.DataFrame(data, columns = [
                "EMPID", "Gender", "Age", "Sales", "BMI", "Income"])


    histogram()
    bar_chart()
    box_plot_chart()
    pie_chart()
    scatter_plot()