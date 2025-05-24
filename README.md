# 📚 Estratégias de Chunking para RAG - Análise Detalhada

##  Visão Geral do Projeto

Este projeto demonstra a implementação prática de diferentes estratégias de chunking (fragmentação de texto) para sistemas de Recuperação Aumentada por Geração (RAG). O objetivo principal é ilustrar a variabilidade entre as principais técnicas de chunking, suas vantagens, desvantagens e casos de uso ideais.

##  Estrutura do Projeto

```
estrategias_chunkings/
├── src/
│   └── estrategias_chunkings/
│       ├── ChunkfixedSize.py
│       ├── ChunkSlidingWindowChunking.py
│       ├── ChunkRecursiveCharacterTextSplitting.py
│       ├── ChunkSemantic.py
│       └── ChunkHiererchical.py
├── tests/
├── pyproject.toml
└── README.md
```


## Estratégias Implementadas

### 1. **Fixed Size Chunking** (`ChunkfixedSize.py`)

#### Descrição
Divide o texto em fragmentos de tamanho fixo baseado no número de caracteres.

#### ✅ Vantagens
- **Simplicidade**: Fácil de implementar e entender
- **Previsibilidade**: Tamanho consistente dos chunks
- **Performance**: Rápido processamento sem análise complexa
- **Controle de memória**: Uso previsível de recursos

#### ❌ Desvantagens
- **Quebra de contexto**: Pode dividir frases no meio
- **Perda semântica**: Não considera o significado do texto
- **Qualidade inferior**: Chunks podem ter informações incompletas

#### 🎯 Caso de Uso Ideal
- Textos simples e uniformes
- Quando a velocidade é prioritária
- Processamento em lote de grandes volumes

---

### 2. **Sliding Window Chunking** (`ChunkSlidingWindowChunking.py`)

#### Descrição
Cria chunks com sobreposição entre eles, mantendo contexto compartilhado.

#### ✅ Vantagens
- **Preservação de contexto**: Sobreposição mantém informações relacionadas
- **Melhor continuidade**: Reduz perda de informação nas bordas
- **Flexibilidade**: Ajuste fino do overlap para diferentes necessidades
- **Robustez**: Menos sensível a quebras arbitrárias

#### ❌ Desvantagens
- **Redundância**: Informação duplicada aumenta armazenamento
- **Custo computacional**: Mais processamento devido ao overlap
- **Complexidade de busca**: Pode retornar resultados duplicados

#### Caso de Uso Ideal
- Documentos com narrativa contínua
- Quando contexto é crítico
- Análise de sentimento ou tópicos

---

### 3. **Recursive Character Text Splitting** (`ChunkRecursiveCharacterTextSplitting.py`)

#### Descrição
Divide texto recursivamente usando múltiplos separadores hierárquicos (parágrafos, frases, palavras).

#### ✅ Vantagens
- **Respeita estrutura**: Mantém integridade de parágrafos e seções
- **Inteligência na divisão**: Usa separadores naturais do texto
- **Versatilidade**: Adapta-se a diferentes formatos de documento
- **Qualidade superior**: Chunks mais coerentes e completos

#### ❌ Desvantagens
- **Tamanho variável**: Chunks podem ter tamanhos muito diferentes
- **Complexidade**: Mais difícil de configurar otimamente
- **Performance**: Processamento mais lento que fixed-size

#### Caso de Uso Ideal
- Documentos estruturados (markdown, HTML)
- Textos técnicos e acadêmicos
- Quando qualidade é prioritária

---

### 4. **Semantic Chunking** (`ChunkSemantic.py`)

#### Descrição
Utiliza embeddings e similaridade semântica para agrupar conteúdo relacionado.

#### ✅ Vantagens
- **Coerência máxima**: Mantém ideias relacionadas juntas
- **Inteligência semântica**: Compreende o significado do texto
- **Qualidade de recuperação**: Melhores resultados em RAG
- **Adaptabilidade**: Funciona bem com diversos tipos de conteúdo

#### ❌ Desvantagens
- **Custo computacional**: Requer modelo de embeddings
- **Latência**: Processamento significativamente mais lento
- **Dependência de API**: Pode requerer serviços externos
- **Custo financeiro**: APIs de embedding podem ser caras

#### Caso de Uso Ideal
- Bases de conhecimento complexas
- Quando precisão é crítica
- Documentos com múltiplos tópicos entrelaçados

---

### 5. **Hierarchical Chunking** (`ChunkHiererchical.py`)

#### Descrição
Cria múltiplos níveis de chunks, do mais geral ao mais específico.

#### ✅ Vantagens
- **Multi-resolução**: Diferentes níveis de detalhe
- **Navegação eficiente**: Busca hierárquica otimizada
- **Contexto completo**: Mantém visão macro e micro
- **Flexibilidade de busca**: Pode recuperar em diferentes granularidades

#### ❌ Desvantagens
- **Complexidade de implementação**: Mais difícil de configurar
- **Armazenamento**: Múltiplas versões do mesmo conteúdo
- **Gestão complexa**: Requer lógica sofisticada de recuperação
- **Overhead computacional**: Processamento em múltiplos níveis

#### Caso de Uso Ideal
- Documentação técnica extensa
- Sistemas de FAQ multi-nível
- Bases de conhecimento corporativas

---

## 📊 Tabela Comparativa

| Estratégia | Complexidade | Preservação de Contexto | Velocidade | Custo | Qualidade RAG |
|------------|--------------|------------------------|------------|--------|---------------|
| Fixed Size | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐ |
| Sliding Window | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Recursive | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Semantic | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Hierarchical | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

##  Recomendações de Uso

### Para Iniciantes
Comece com **Fixed Size** ou **Recursive Character Text Splitting** para entender os conceitos básicos.

### Para Produção
1. **Documentos simples**: Use Recursive Character Text Splitting
2. **Alta precisão**: Implemente Semantic Chunking
3. **Grandes volumes**: Considere Hierarchical com cache

### Otimização de Performance
- Combine estratégias: Use Recursive para divisão inicial e Semantic para refinamento
- Implemente cache de embeddings para Semantic Chunking
- Use processamento assíncrono para grandes volumes