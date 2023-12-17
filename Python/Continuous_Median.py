import heapq
    
def median_counter(array):
    min_heap = []  # Min-heap for den større halvdelen av elementene
    max_heap = []  # Max-heap for den mindre halvdelen av elementene
    median_sum = 0  # Summen av medianene

    for num in array:
        # Legg til elementet i riktig heap
        if not max_heap or num < -max_heap[0]:
            # Legg til i max-heap med negativ verdi
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)  # Legg til i min-heap

        # Balanser heapene hvis nødvendig
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Beregn medianen og legg den til i summen
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) // 2
        else:
            median = -max_heap[0]
        median_sum += median

    return median_sum


inp = int(input())
while inp > 0:
    l = int(input())
    liste = list(map(int,input().split()))
    print(median_counter(liste))
    inp -= 1