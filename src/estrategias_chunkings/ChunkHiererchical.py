from langchain_text_splitters import RecursiveCharacterTextSplitter


class HierarchicalChunker:
    """
    Implementa chunking hierárquico com múltiplos níveis
    """
    def __init__(self, levels=[1000, 500, 200]):
        self.levels = sorted(levels, reverse=True)
    
    def create_hierarchy(self, text):
        hierarchy = {}
        
        # Nível 1: Documento completo ou seções grandes
        level1_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.levels[0],
            chunk_overlap=100
        )
        level1_chunks = level1_splitter.split_text(text)
        
        hierarchy['level_1'] = level1_chunks
        
        # Nível 2: Parágrafos ou subseções
        hierarchy['level_2'] = []
        for chunk in level1_chunks:
            level2_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.levels[1],
                chunk_overlap=50
            )
            sub_chunks = level2_splitter.split_text(chunk)
            hierarchy['level_2'].extend(sub_chunks)
        
        # Nível 3: Sentenças ou detalhes
        hierarchy['level_3'] = []
        for chunk in hierarchy['level_2']:
            level3_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.levels[2],
                chunk_overlap=20
            )
            detail_chunks = level3_splitter.split_text(chunk)
            hierarchy['level_3'].extend(detail_chunks)
        
        return hierarchy

# Exemplo de uso
texto_exemplo = """
# Inteligência Artificial em Saúde

## Diagnóstico por Imagem
A IA revolucionou o diagnóstico médico através da análise de imagens.
Algoritmos de deep learning conseguem detectar anomalias com precisão superior a 95%.

### Aplicações em Radiologia
- Detecção de tumores
- Análise de fraturas
- Identificação de pneumonia

## Medicina Personalizada
Tratamentos customizados baseados em dados genéticos do paciente.
"""

hierarchical_chunker = HierarchicalChunker()
hierarchy = hierarchical_chunker.create_hierarchy(texto_exemplo)

print(f"Nível 1: {len(hierarchy['level_1'])} chunks grandes")
print(f"Nível 2: {len(hierarchy['level_2'])} chunks médios")
print(f"Nível 3: {len(hierarchy['level_3'])} chunks pequenos")