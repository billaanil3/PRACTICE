from wordcloud import WordCloud
import matplotlib.pyplot as plt

#text1 = "Ajay Amit Anil Animesh Ankush Archana Arun Gaurav John Kishen Mahalaksmi Murthy Naiju Narasimha Nataraj Praveen Rasmeet Rigved Shanthi Sujatha Thiru Urvashi"
text = " Archana Arun Gaurav John Kishen Naiju Narasimha Nataraj Murthy Rasmeet Rigved Shanthi Sujatha Thiru Urvashi Mahalaksmi Praveen Ankush Anil Ajay Animesh Amit"
cloud = WordCloud(background_color = "white").generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()
