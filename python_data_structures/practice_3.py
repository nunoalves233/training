#Slice list into 3 equal chunks and reverse each chunk

SAMPLE_LIST = [11, 45, 8, 23, 14, 12, 78, 45, 89]

CHUNK_SIZE = int(len(SAMPLE_LIST) / 3)
START = 0
END = CHUNK_SIZE

for i in [1,2,3]:
    # get indexes
    INDEXES = slice(START, END)
    
    # get chunk
    LIST_CHUNK = SAMPLE_LIST[INDEXES]
    print("Chunk", i, LIST_CHUNK)
    
    # reverse chunk
    print("After reversing it", list(reversed(LIST_CHUNK)))

    START = END
    END += CHUNK_SIZE

    