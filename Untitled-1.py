# Data for the pie chart
total_vulnerabilities = [
    sum(critical),
    sum(high),
    sum(medium),
    sum(low),
    sum(info)
]

severity_labels = ['Critical', 'High', 'Medium', 'Low', 'Info']
colors = ['red', 'orange', 'yellow', 'lightblue', 'green']
explode = (0.1, 0.1, 0, 0, 0)  # Highlight Critical and High

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(total_vulnerabilities, labels=severity_labels, autopct='%1.1f%%', startangle=140, 
       colors=colors, explode=explode, shadow=True)
ax.set_title('Vulnerability Severity Distribution for Petty Pills', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()
