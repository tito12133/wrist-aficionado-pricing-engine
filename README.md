# Wrist Aficionado - Pricing Intelligence Engine

A luxury watch marketplace pricing intelligence dashboard built with Python and Streamlit. Provides real-time market analysis, opportunity detection, and margin calculation for secondary market luxury timepieces.

## Features

- **Real-time Price Tracking**: Monitor floor prices across multiple luxury watch references
- **Market Distribution Analysis**: Visualize geographic market concentration and trends
- **Opportunity Detection**: Automatically identify below-market listings with high margin potential
- **Advanced Filtering**: Filter by reference number, condition, year, price range
- **Margin Calculator**: Calculate optimal list prices and profit margins
- **Data Export**: Export filtered intelligence data for team collaboration

## Technology Stack

- **Python 3.13**
- **Streamlit** - Interactive dashboard framework
- **Plotly** - Professional data visualizations
- **Pandas** - Data manipulation and analysis

## Installation
```bash
# Clone repository
git clone https://github.com/tito12133/wrist-aficionado-pricing-engine.git
cd wrist-aficionado-pricing-engine

# Install dependencies
pip install streamlit pandas plotly

# Generate sample data
python generate_sample_data.py

# Run dashboard
streamlit run dashboard.py
```

## Usage

The dashboard launches in your browser at `http://localhost:8501`

### Filters
- **Reference Numbers**: Select specific watch models to analyze
- **Condition**: Filter by condition (New, Unworn, Very Good, Good, Fair)
- **Price Range**: Set minimum and maximum price thresholds
- **Year**: Filter by production year

### Metrics
- **Listings**: Total active listings matching filters
- **Average**: Market average price
- **Floor**: Lowest available price
- **Targets**: Number of below-market opportunities

### Analysis Views
- **Price Distribution**: Box plot showing price ranges by model and condition
- **Geographic Distribution**: Market concentration by location
- **Price Trends**: Historical price movement over time
- **Acquisition Targets**: Below-market listings with calculated margins

## Future Enhancements

- Live marketplace scraping (Chrono24, eBay)
- Multi-currency support with real-time conversion
- Predictive pricing using machine learning
- Slack/email alerts for high-value opportunities
- Seller trust score integration
- Historical trend analysis and forecasting

## Demo

This version uses sample data to demonstrate functionality. Production implementation would integrate with live marketplace APIs and web scraping infrastructure.

## Contact

Built for demonstration purposes - showcasing data analysis, visualization, and dashboard development skills for luxury marketplace intelligence applications.

