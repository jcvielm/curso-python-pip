import matplotlib.pyplot as plt 
# Esta librería que no viene incorporada en python. Se debe instalar. 

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', pctdistance=1.25, labeldistance=.6)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 200]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
