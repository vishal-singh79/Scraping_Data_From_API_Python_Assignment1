```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Scraping Data From API – Python Assignment</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: #0d1117;
      color: #c9d1d9;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
    }

    .container {
      max-width: 900px;
      margin: auto;
    }

    h1, h2, h3 {
      color: #58a6ff;
      border-bottom: 1px solid #30363d;
      padding-bottom: 6px;
    }

    code, pre {
      background-color: #161b22;
      color: #c9d1d9;
      padding: 10px;
      border-radius: 6px;
      overflow-x: auto;
    }

    pre {
      margin: 15px 0;
    }

    ul {
      margin-left: 20px;
    }

    .section {
      margin-bottom: 30px;
    }

    footer {
      text-align: center;
      margin-top: 40px;
      font-size: 14px;
      color: #8b949e;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Scraping Data From API – Python Assignment</h1>

    <div class="section">
      <h2>Overview</h2>
      <p>
        This project demonstrates how to extract data from an external API using
        Python, clean and validate the data, and store it in a structured format.
        The project follows a modular and scalable structure commonly used in
        real-world data engineering tasks.
      </p>
    </div>

    <div class="section">
      <h2>Features</h2>
      <ul>
        <li>API data extraction</li>
        <li>Exception handling for unreliable APIs</li>
        <li>Data cleaning and transformation</li>
        <li>Data validation rules</li>
        <li>Execution logging</li>
        <li>Structured project layout</li>
      </ul>
    </div>

    <div class="section">
      <h2>Tech Stack</h2>
      <ul>
        <li>Python 3</li>
        <li>Requests</li>
        <li>Pandas</li>
        <li>SQLite</li>
        <li>Logging</li>
      </ul>
    </div>

    <div class="section">
      <h2>Project Structure</h2>
      <pre>
Scraping_Data_From_API_Python_Assignment1/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   └── main.py
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
      </pre>
    </div>

    <div class="section">
      <h2>Prerequisites</h2>
      <ul>
        <li>Python 3.8 or higher</li>
        <li>pip package manager</li>
      </ul>
    </div>

    <div class="section">
      <h2>Installation & Setup</h2>
      <h3>Clone Repository</h3>
      <pre>git clone https://github.com/vishal-singh79/Scraping_Data_From_API_Python_Assignment1.git
cd Scraping_Data_From_API_Python_Assignment1</pre>

      <h3>Create Virtual Environment</h3>
      <pre>python -m venv venv</pre>

      <h3>Activate Virtual Environment</h3>
      <pre>Linux / macOS: source venv/bin/activate
Windows: venv\Scripts\activate</pre>

      <h3>Install Dependencies</h3>
      <pre>pip install -r requirements.txt</pre>
    </div>

    <div class="section">
      <h2>Run the Project</h2>
      <pre>cd src
python main.py</pre>
    </div>

    <div class="section">
      <h2>Output</h2>
      <ul>
        <li>Processed data is saved in the <code>data/</code> directory</li>
        <li>Logs display execution status and errors</li>
        <li>Invalid or duplicate records are rejected</li>
      </ul>
    </div>

    <div class="section">
      <h2>API Used</h2>
      <pre>https://jsonplaceholder.typicode.com/users</pre>
    </div>

    <footer>
      <p>Author: Vishal Singh</p>
      <p>For educational and learning purposes only</p>
    </footer>
  </div>
</body>
</html>
```
