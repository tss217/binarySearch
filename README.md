README - Comparação de Algoritmos de Busca

Este é um programa Python que demonstra a diferença de desempenho entre quatro algoritmos de busca diferentes: Busca Binária, Busca Sequencial, Busca com a Biblioteca bisect e Busca com a Biblioteca numpy. O programa gera dados de tempo para cada algoritmo de busca ao longo do tempo e os armazena em um arquivo CSV.
Algoritmos de Busca Implementados
Busca Binária (binarySearch)

    A busca binária é um algoritmo eficiente para encontrar um elemento em uma lista ordenada.
    O algoritmo divide repetidamente a lista ao meio e compara o elemento alvo com o elemento do meio da lista.
    O tempo gasto é medido e armazenado.

Busca Sequencial (sequentialSearch)

    A busca sequencial é um algoritmo simples que percorre a lista do início ao fim, comparando cada elemento com o elemento alvo.
    O tempo gasto é medido e armazenado.

Busca com bisect (bisectSearch)

    A biblioteca bisect fornece uma função eficiente para encontrar a posição de inserção de um elemento em uma lista ordenada.
    O algoritmo usa a função bisect.bisect para encontrar a posição de inserção e verifica se o elemento alvo está presente na lista.
    O tempo gasto é medido e armazenado.

Busca com numpy (numpySearch)

    A biblioteca numpy fornece uma função de busca eficiente para encontrar a posição de inserção de um elemento em um array ordenado.
    O algoritmo usa a função numpy.searchsorted para encontrar a posição de inserção e verifica se o elemento alvo está presente no array.
    O tempo gasto é medido e armazenado.

Uso do Programa

    O programa começa criando uma lista lst de tamanho lstRange e preenchendo-a com números de 0 a lstRange-1.
    Em seguida, ele entra em um loop que executa 200 vezes.
    Para cada iteração do loop, ele chama os quatro algoritmos de busca (binarySearch, sequentialSearch, bisectSearch e numpySearch) e mede o tempo gasto em cada busca.
    Os resultados são armazenados em um arquivo CSV com o nome fornecido, que é especificado como name. Os resultados incluem o tempo gasto em cada algoritmo de busca para a pesquisa do número num.

Executando o Programa

Para executar o programa, você precisa ter o Python instalado em seu sistema. Basta copiar e colar o código em um arquivo Python (.py) e executá-lo. Certifique-se de que as bibliotecas necessárias (pandas, numpy) estejam instaladas.
