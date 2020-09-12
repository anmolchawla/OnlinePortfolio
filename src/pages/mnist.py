import streamlit as st
from streamlit_drawable_canvas import st_canvas
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from statistics import mean
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb
import altair as alt
import pandas as pd

def write():
    mnistAlgo = ['SVM', 'Logistic Regression', 'Decision Tree', 'Random Forest', 'Naive Bayes', 'XG Boost']
    stroke_width = st.sidebar.slider("Stroke width: ",5, 10, 5)
    realtime_update = False
    update_button = False

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        background_color="#FAFAFA",
        stroke_color="#000000",
        update_streamlit=realtime_update or update_button,
        height=300,
        width=300,
        drawing_mode="freedraw",
        key="canvas",
    )

    if not realtime_update:
        update_button = st.button('Predict')

    if canvas_result.image_data is not None:
        print(canvas_result.image_data)





    digits = datasets.load_digits()
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)

    svmclf = svm.SVC(gamma=0.001).fit(X_train, y_train)
    logisticclf = LogisticRegression(solver='newton-cg', random_state=0, max_iter=1000).fit(X_train, y_train)
    decisionclf = DecisionTreeClassifier(random_state=0).fit(X_train, y_train)
    randomclf = RandomForestClassifier(max_depth=2, random_state=0).fit(X_train, y_train)
    nbayeclf = GaussianNB().fit(X_train, y_train)
    xgbclf = xgb.XGBClassifier(objective="multi:softprob", random_state=42).fit(X_train, y_train)

    clfs = {'svmclf': svmclf, 'logisticclf': logisticclf, 'decisionclf': decisionclf, 'randomclf': randomclf,
            'nbayeclf': nbayeclf, 'xgbclf': xgbclf}
    clfmetrics = {'accuracy': [], 'precision': [], 'recall': [], 'f1-score': []}
    graphs =  {'accuracy': [], 'precision': [], 'recall': [], 'f1-score': []}
    measures = {'accuracy': metrics.accuracy_score, 'precision': metrics.precision_score,
                'recall': metrics.recall_score, 'f1-score': metrics.f1_score}
    for clf in clfs.keys():
        for clfmetric in clfmetrics.keys():
            y_pred = clfs[clf].predict(X_test)
            if clfmetric == "accuracy":
                val = 100*measures[clfmetric](y_test, y_pred)
            else:
                val = measures[clfmetric](y_test, y_pred, average='macro')
            fval = val if type(val) is not list else mean(val)
            clfmetrics[clfmetric].append(round(fval, 3))

    for met in list(clfmetrics.keys()):
        source = pd.DataFrame()
        source['Algo'] = mnistAlgo
        source[met] = clfmetrics[met]
        graphs[met] = alt.Chart(source).mark_bar().encode(x='Algo', y=met).properties(width=500, height=300).interactive()
    st.altair_chart(alt.hconcat(graphs['accuracy'],graphs['precision']))
    st.altair_chart(alt.hconcat(graphs['recall'],graphs['f1-score']))

