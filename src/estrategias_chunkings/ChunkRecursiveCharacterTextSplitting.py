from langchain.text_splitter import RecursiveCharacterTextSplitter

'''
Este código divide um texto estruturado em partes (chunks) usando o RecursiveCharacterTextSplitter da biblioteca langchain. O texto inclui seções e itens em lista sobre aplicações da IA. O splitter é configurado para:
Dividir o texto em chunks de até 150 caracteres.
Manter uma sobreposição de 30 caracteres entre os chunks para preservar o contexto.
Usar vários separadores como quebras de linha duplas, quebras de linha, pontos, espaços e strings vazias para determinar onde dividir o texto.
O resultado são chunks menores que mantêm a estrutura e o contexto do texto original, úteis para processamento de texto em NLP.

'''

texto_estruturado = """
# Introdução à IA

A inteligência artificial representa um marco na evolução tecnológica.

## Aplicações Principais

### Saúde
- Diagnóstico assistido por IA
- Descoberta de medicamentos
- Análise de imagens médicas

### Finanças
- Detecção de fraudes
- Trading algorítmico
- Análise de crédito
"""

splitter_recursivo = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = splitter_recursivo.split_text(texto_estruturado)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}")
    print(f"Tamanho: {len(chunk)} caracteres\n---\n")