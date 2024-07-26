import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize():
    # Define the data
    data = [
        ["Total services", 325.3, 182.0, 341.1, 178.3],
        ["Manufacturing services on physical inputs", 1.5, 0.2, 1.4, 0.1],
        ["owned by others", None, None, None, None],  # Placeholder for the split
        ["Maintenance and repair services n.i.e.", 0.2, 1.9, 0.2, 1.5],
        ["Transport", 36.1, 40.6, 29.2, 29.3],
        ["Travel", 27.0, 28.4, 33.7, 33.7],
        ["Construction", 3.8, 2.8, 4.6, 2.8],
        ["Insurance and pension services", 3.3, 2.3, 3.3, 2.9],
        ["Financial services", 7.8, 5.7, 8.1, 4.6],
        ["Charges for the use of intellectual property n.i.e.", 1.3, 10.6, 1.6, 15.0],
        ["Telecommunications, computer, and information services", 152.3, 19.8, 163.6, 20.9],
        ["Other business services", 80.4, 59.7, 88.6, 59.3],
        ["Personal, cultural, and recreational services", 3.9, 5.5, 4.4, 6.3],
        ["Government goods and services n.i.e.", 0.7, 1.0, 0.6, 1.1],
        ["Others n.i.e.", 7.1, 3.4, 1.8, 0.8]
    ]

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Service", "Import 2023", "Exports 2023", "Import 2024", "Exports 2024"])

    # Fill missing values in 'owned by others'
    df['Service'] = df['Service'].fillna(method='ffill')

    # Drop the placeholder row
    df = df[df['Service'] != 'owned by others']

    # Save Bar Chart of Imports and Exports in 2023 and 2024
    plt.figure(figsize=(14, 10))
    df.plot(kind='bar', x='Service', y=['Import 2023', 'Exports 2023', 'Import 2024', 'Exports 2024'], figsize=(14, 10),
            ax=plt.gca())
    plt.title('Imports and Exports in 2023 and 2024')
    plt.xlabel('Service')
    plt.ylabel('Value')
    plt.xticks(rotation=90)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('images/imports_exports_2023_2024.png')  # Save the bar chart
    plt.close()

    # Save Line Plot for Imports Comparison Over Years
    plt.figure(figsize=(14, 7))
    df.set_index('Service')[['Import 2023', 'Import 2024']].plot(kind='line', marker='o', ax=plt.gca())
    plt.title('Imports Comparison 2023 vs 2024')
    plt.xlabel('Service')
    plt.ylabel('Import Value')
    plt.xticks(rotation=90)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('images/imports_comparison_2023_2024.png')  # Save the imports comparison line plot
    plt.close()

    # Save Line Plot for Exports Comparison Over Years
    plt.figure(figsize=(14, 7))
    df.set_index('Service')[['Exports 2023', 'Exports 2024']].plot(kind='line', marker='o', ax=plt.gca())
    plt.title('Exports Comparison 2023 vs 2024')
    plt.xlabel('Service')
    plt.ylabel('Export Value')
    plt.xticks(rotation=90)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('images/exports_comparison_2023_2024.png')  # Save the exports comparison line plot
    plt.close()

    # Save Heatmap of the Data
    plt.figure(figsize=(14, 7))
    sns.heatmap(df[['Import 2023', 'Exports 2023', 'Import 2024', 'Exports 2024']].set_index(df['Service']), annot=True,
                cmap='coolwarm', cbar=True, ax=plt.gca())
    plt.title('Heatmap of Service Values')
    plt.tight_layout()
    plt.savefig('images/heatmap_service_values.png')  # Save the heatmap
    plt.close()
