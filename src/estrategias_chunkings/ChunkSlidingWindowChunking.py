def sliding_window_chunk(texto, tamanho_chunk=100, sobreposicao=30):
    """
    Implementa chunking com janela deslizante
    """
    palavras = texto.split()
    chunks = []

    i = 0
    while i < len(palavras):
        fim = min(i + tamanho_chunk, len(palavras))
        chunk = ' '.join(palavras[i:fim])
        chunks.append(chunk)
        i += tamanho_chunk - sobreposicao

    return chunks

# Exemplo de uso
texto_continuo = """
O aprendizado profundo revolucionou a inteligência artificial nos últimos anos.
Redes neurais profundas conseguem aprender representações complexas dos dados.
Transformers como GPT e BERT estabeleceram novos padrões em processamento de linguagem.
A capacidade de processar sequências longas melhorou significativamente.
Aplicações práticas incluem tradução automática e geração de texto.
"""

chunks_janela = sliding_window_chunk(texto_continuo, tamanho_chunk=15, sobreposicao=5)

for i, chunk in enumerate(chunks_janela):
    print(f"Chunk {i+1} (janela deslizante):")
    print(f"'{chunk}'")
    print(f"Palavras: {len(chunk.split())}\n")