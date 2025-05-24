from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

# Configuração do semantic chunker
'''
Divide o texto baseado em similaridade semântica, mantendo ideias relacionadas juntas.
Usa embeddings do OpenAI para calcular similaridade.
Mantém chunks que são semanticamente relevantes.

No exemplo, o texto é dividido em chunks que mantêm ideias relacionadas, como "IA" e "linguagem natural".

'''




# Texto com múltiplos tópicos
texto_semantico = """
O processamento de linguagem natural permite que computadores entendam texto humano.
Técnicas como tokenização e análise sintática são fundamentais.
Modelos de linguagem como BERT revolucionaram o campo.

A visão computacional é outra área importante da IA.
Redes neurais convolucionais processam imagens eficientemente.
Aplicações incluem reconhecimento facial e veículos autônomos.

O aprendizado por reforço treina agentes através de recompensas.
Algoritmos como Q-learning e policy gradient são populares.
Jogos e robótica são domínios comuns de aplicação.
"""

# Configuração do semantic chunker
embeddings = OpenAIEmbeddings()
semantic_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95
)

# Criando chunks semânticos
chunks = semantic_splitter.split_text(texto_semantico)

for i, chunk in enumerate(chunks):
    print(f"Chunk Semântico {i+1}:")
    print(chunk)
    print(f"\nTamanho: {len(chunk)} caracteres\n{'='*50}\n")