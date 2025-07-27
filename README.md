# Mini RAG
Esta aplicación utiliza el modelo RAG (Retrieval-Augmented Generation) para buscar citas de filósofos que mejor se adhieran al prompt del usuario, para que un LLM produzca una reflexión sobre el contexto recuperado y el prompt original.
## ¿Cómo se utiliza?
1. Clonamos el repositorio
2. Descargamos las dependencias
3. Cargamos la base de datos vectorial de Chroma
4. Generamos una reflexión filosófica
```
git clone https://github.com/agostinaines/MiniRAG.git
pip install -r requirements.txt
pip loadDB.py
pip generator.py
```
Es de destacar que se utilizan dos modelos de generación distintos dentro del generator.py: 'gemini-2.5-flash' y 'HuggingFaceTB/SmolLM2-360M'.
## Consideraciones
Me pareció mucho más fácil trabajar con el modelo de Google que el de Hugging Face, de este último rescato que se puede personalizar mucho más el modelo con distintos parámetros.
