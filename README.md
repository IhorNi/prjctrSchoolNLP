# prjctrSchoolTestCase
Test task for ML in Production course at <a href="https://prjctr.notion.site/Machine-Learning-in-Production-00670943bd054f709cf4789ab8eec8bd">Prjctr School</a>. The goal of this test case is to build an end-to-end solution.

## The milestones of the project are:

### Model
<ul>
    <li>Implement any NLP model for this problem. The final RMSE metric doesn't matter here, the goal here is just to get a trained model.
        <ul>
            <li>Simple Ridge regression model is built upon TfidfVectorized text after basic cleaning steps.</li> 
            <li>Trained models are saved to nlp_models for next steps.</li>            
            <li><b>trained_model.py</b></li>
        </ul>
    </li>
</ul>

### Stage 2 - API
<ul>
    <li>Write an API server for the trained model form Stage1. The API should contain only 1 endpoint for prediction:
        <ul>
            <li>API server is built with Flask-RESTful - <b>app.py</b></li> 
            <li>GET endpoint /get_text_readability?text=<i>your text to test</i></li>
        </ul>
    </li>
</ul>

### Stage 3 - Deploy API
<ul>
    <li>Deploy API from Stage2 and send the endpoint for testing.
        <ul>
            <li>API server is deployed with heroku to https://lit-taiga-89750.herokuapp.com</li> 
            <li>Example of using API - <b>test_deployed_api.py</b></li>
        </ul>
    </li>
</ul>




