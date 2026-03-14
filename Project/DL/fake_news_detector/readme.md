transformers datasets gradio peft torch accelerate bitsandbytes pandas numpy scikit-learn

1. mkdir fake_news_detector && cd fake_news_detector
2. pip install -r requirements.txt
3. python setup.py # Download LIAR dataset
4. python trainer.py # Fine-tune (~20min CPU, 5min GPU)
5. python app.py # http://127.0.0.1:7860
