# StreamDEA

### Differential Expression Analysis (DEA) for RNA-Seq Data

Our web platform enables you to perform Differential Expression Analysis (DEA) on RNA-Seq count data with ease.
Using the powerful pyDESeq module, based on the DESeq2 method, you can quickly analyze gene expression differences between experimental conditions.
Simply upload your count matrix and metadata, and the platform will automatically process your data, identify differentially expressed genes, and provide comprehensive results, including log-fold changes, p-values, and visualizations like volcano plots and heatmaps.
Get started today to uncover the insights hidden in your RNA-Seq data!

### Initializing the project
 - Create conda env with python version 3.12 and activate it ```conda create -n <env_name> python==3.12``` or install python 3.12 into your machine
 - Clone the repository and unzip the repo
 - Install poetry ``` pip install poetry ``` and run the command ``` poetry install ``` from the root dir
 - Use the make command ``` make run ``` or use ``` streamlit run app.py ``` and visit http://localhost:8501


### Input Data Requirements

This application requires two types of input files: **Count Data** and **Metadata**. Below are the details for how each file should be formatted.

---

#### 1. Count Data File
This file contains raw or normalized count data (e.g., gene expression, feature counts) in a tabular format.

#### Structure
- **Rows**: Represent features (e.g., genes, transcripts, or other entities being counted).
- **Columns**: Represent samples or conditions.

#### Content
- The first **column** should contain unique identifiers for the features (e.g., gene names or IDs).
- The first **row** should contain sample names (e.g., sample IDs or experimental conditions).
- Data cells should contain numerical values representing counts or measurements.

#### Example
| Feature/Gene ID | Sample_1 | Sample_2 | Sample_3 |
|------------------|----------|----------|----------|
| Gene_1          | 100      | 120      | 130      |
| Gene_2          | 50       | 60       | 70       |
| Gene_3          | 300      | 290      | 310      |

#### Notes
- Ensure there are **no missing values** in the count matrix.
- Avoid duplicate feature or sample identifiers.

---

#### 2. Metadata File
This file provides additional information about the samples in the count data. Metadata is essential for grouping and analyzing the data based on experimental conditions or other attributes.

#### Supported Formats
- `.tsv`, `.csv`, `.parquet`, `.xlsx`

#### Structure
- **Rows**: Represent individual samples.
- **Columns**: Represent sample attributes (e.g., condition, treatment, batch).

#### Content
- The first **column** should contain sample names or IDs that **exactly match** the column names in the count data file (excluding the first feature ID column).
- The second column should contain **Group or condition** (e.g., control, treated)
- Additional columns can include:
- **Batch information** (Optional)
- **Time points** (Optional)
- Any other relevant experimental metadata.

#### Example
| Sample ID | Condition | Batch  | Timepoint |
|-----------|-----------|--------|-----------|
| Sample_1  | Control   | Batch_1| 0h        |
| Sample_2  | Treated   | Batch_1| 6h        |
| Sample_3  | Treated   | Batch_2| 12h       |

#### Notes
- Ensure **no missing values** in the metadata table.
- Ensure sample IDs in the metadata **exactly match** the column headers in the count data.


### About

This project is designed to streamline RNA-seq data analysis by leveraging modern bioinformatics tools and interactive interfaces. The application provides an efficient and user-friendly solution for tasks such as differential expression analysis, data visualization, and functional enrichment.

---

#### Key Technologies Used

#### 1. [PyDESeq2](https://pydeseq2.readthedocs.io/)
- PyDESeq2 is a Python library that implements the DESeq2 algorithm for differential gene expression analysis. 
- Built for bioinformaticians, it simplifies the process of working with count data, providing efficient and accurate results while maintaining compatibility with Python workflows.
- Version used: **v0.4.12**

#### 2. [Streamlit](https://streamlit.io/)
- Streamlit is an open-source Python library for building data-driven web applications.
- It allows for the creation of interactive dashboards and visualization tools with minimal coding effort, enabling seamless integration of user input and real-time computation.
- Used to develop the application's graphical interface for improved usability.

---

### Author

- **Mohamed Sinan M**  
- Email: [mohamedysf@bicpu.edu.in](mailto:mohamedysf@bicpu.edu.in)  
- Contributed to the design, implementation, and documentation of this project.

---

