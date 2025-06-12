# DU-Capstone

# Consumer Expenditure Analysis

## Project Overview

This project focuses on analyzing consumer expenditure data provided by the **U.S. Bureau of Labor Statistics (BLS)**. The goal is to extract, clean, and visualize spending trends across different age groups over time. It includes the following components:

- Data extraction and transformation from `.xlsx` files.
- Aggregation and preparation of data across multiple years.
- Visualization of trends and patterns across consumer age groups

## Motivation and Research Question

In recent discourse, inflation is often portrayed as severely impacting the average American—especially the youth. However, these narratives may oversimplify or misrepresent the truth. This project seeks to use **data-driven analysis** to evaluate those claims, using age-based spending trends as a proxy for economic resilience and lifestyle continuity. I hope to answer the question: How have consumer expenditures by age group evolved over time, and do these trends support or contradict popular narratives about inflation and economic well-being?

## Data Source

- **Main Data Tables**: [BLS Consumer Expenditure Tables](https://www.bls.gov/cex/tables.htm)
- **Consumer Unit Definition**: [BLS Consumer Unit Concepts](https://www.bls.gov/opub/hom/cex/concepts.htm)

- Focuses on specific age groups: 25-34, 35-44, 45-54, 55-64, and 65-74.

## Key Findings

- **Housing**: Expenditures rose over the decade, especially post-2016, yet **home ownership rates remained steady**, contradicting the idea that corporations are buying all homes.
- **Food & Alcohol**: While costs rose, the **share of total expenditures remained constant**, signaling stable consumer behavior and suggesting that food inflation may not be as severe as reported.
- **Dining Out**: Spending dropped during COVID but has recovered, pointing to resilient consumer preferences.
- **Entertainment & Apparel**: Spending dipped during COVID but rebounded afterward—typical of a **recovering economy**.
- **Healthcare**: Despite rising costs, the **income-to-healthcare expenditure ratio** remained constant, undermining the narrative of runaway healthcare expenses.
- **Income vs. Expenditure**: Most age groups maintained a **surplus**, with income outpacing spending even through economic turbulence like the Trump Presidency and COVID.
By examining not just raw expenditure but also **ratios relative to income**, this analysis shows that increases in expenses often parallel increases in income and the economy, for the average American, is **more stable than media narratives suggest**.

## Project Structure

```
.
├── Data/                 # Contains raw Excel data files from BLS
├── Scripts/
│   └── helper.py         # Functions for loading and processing data
│   └── grapher.py        # Visualization utilities
├── Main.ipynb            # Main analysis notebook
└── README.md             # Project overview (this file)
```

## Dependencies

- Python 3.x
- pandas
- matplotlib / seaborn 

## License

This project is for educational and research use. Check the BLS data usage policies for redistribution or commercial use.
