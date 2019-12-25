def best_stock(a):
    d3={v:k for k,v in a.items()}
    return d3[max(d3)]

if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))
