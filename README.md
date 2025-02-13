# Wikipedia Knowledge Graph Builder

A tool that crawls Wikipedia pages starting from a user-defined entry point, collecting links and content to build a knowledge graph visualization. The project transforms Wikipedia's interconnected pages into an explorable network visualization resembling a neural network.

![image](https://github.com/user-attachments/assets/4db1bb93-56ba-4016-ac02-bb5948c21d25)


## Features

- **Recursive Web Scraping**: Starts from a user-defined Wikipedia page and recursively follows links to build a comprehensive dataset
- **Data Collection**: 
  - Extracts all links from each page
  - Downloads complete HTML content
  - Converts HTML to Markdown for better readability
  - Generates CSV files containing page relationships
- **Interactive Visualization**:
  - Brain-like network graph implemented in Java
  - Visual representation of page connections
  - Intuitive navigation through the knowledge graph

## Getting Started

### Prerequisites

- Java Development Kit (JDK)
- Required Python packages (if using Python for scraping)
- Network connection for Wikipedia access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wiki-knowledge-graph.git
cd wiki-knowledge-graph
```

2. Install dependencies (if using Python for scraping):
```bash
pip install -r requirements.txt
```

### Usage

1. Start the scraper with your chosen Wikipedia page:
```bash
python scraper.py --start-page "Your_Wikipedia_Page_Title"
```

2. Run the visualization:
```bash
cd visualization/java
javac GraphVisualizer.java
java GraphVisualizer
```

## Data Format

### CSV Structure
The CSV files contain the following information:
- Source page
- Target page
- Link type
- Additional metadata

### Visualization Features
- Node size represents page importance
- Edge thickness shows connection strength
- Interactive zooming and panning
- Node clustering for related topics

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Wikipedia for providing the vast knowledge base
- Contributors and maintainers
- Open source community for inspiration and tools

## Contact

Florian Demartini - florian.demartini.dev@gmail.com

# Wiki-Scrap
Scrap data from wikipedia

starts with the page defined by the user and continues to infinity starting with the nearest pages











## Galery
![image](https://github.com/user-attachments/assets/000ab363-b2d0-41f5-a897-774982861b22)


