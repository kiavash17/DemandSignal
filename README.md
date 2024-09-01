
# **ExplorerBee: AI-Driven Demand Forecasting Platform**

ExplorerBee is an AI-driven demand forecasting platform designed to help startups identify their first 10 customers and refine their offerings based on real market needs. The platform integrates NLP-based analysis, LinkedIn profile scraping, automated outreach, A/B testing, response tracking, and feedback collection to provide actionable insights and continuous improvement suggestions for startups.

## **Features**

1. **Startup Onboarding and Information Gathering:**
   - User-friendly form for startups to submit their details, including UVP, target audience, and industry.
   - Data stored in a structured SQLite database.

2. **LinkedIn Analytics and Targeting:**
   - Automated scraping and analysis of LinkedIn profiles based on startup's market needs.
   - Segmentation of profiles into categories like executives, managers, and engineers for targeted outreach.

3. **Automated Outreach and A/B Testing:**
   - Automated messaging system for outreach using tailored messages.
   - A/B testing to evaluate different versions of messages for engagement effectiveness.

4. **Response Tracking and Feedback Collection:**
   - Real-time tracking of responses and engagement metrics.
   - Collection of feedback from recipients to refine outreach strategies.

5. **Analytics Dashboard:**
   - Visual insights and analytics dashboard to monitor outreach performance and feedback.
   - Refinement suggestions based on performance data and feedback.

6. **Support and Guidance:**
   - Comprehensive user guides, support channels, and training materials to help startups leverage the platform effectively.

## **Getting Started**

### **Prerequisites**

- Python 3.7 or higher
- pip (Python package installer)
- Flask and other required Python packages (listed in `requirements.txt`)

### **Installation**

1. **Clone the Repository:**

```bash
git clone https://github.com/your-username/ExplorerBee.git
cd ExplorerBee
```

2. **Run the Setup Script:**

Use the provided `setup.sh` script to automatically install all necessary dependencies and set up the environment. Make sure to run this script with `sudo` to install system-level dependencies:

For Linux/macOS:
```bash
sudo bash setup.sh
```

This script will install Python3, pip, necessary Python packages, and the spaCy English model.

### **Running the Application**

1. **Start the Flask Application:**

```bash
python explorerbee.py
```

2. **Access the Platform:**

Open your web browser and go to `http://127.0.0.1:5000/` to start using the ExplorerBee platform.

### **Using the Platform**

- **Submit Startup Information:** Navigate to the home page and fill out the form with your startup's details.
- **View Analytics:** After submitting your information, access the analytics dashboard to see the results of your outreach campaigns.
- **Refine Strategy:** Use the insights and refinement suggestions provided by the platform to improve your offering and outreach strategy.

### **Support and Documentation**

- **User Guide:** [User Guide](static/user_guide.md)
- **Contact Support:** Reach out via the support form on the platform or email [support@explorerbee.com](mailto:support@explorerbee.com).

### **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

### **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
