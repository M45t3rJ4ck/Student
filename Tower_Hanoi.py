def towers(n, start, spare, end):
    print("Tower ", n, start, spare, end, " called")
    if n > 0:
        towers(n - 1, start, end, spare)
        if start[0]:
            disk = start[0].pop()
            print("Move " + str(disk) + " from: " + start[1] + " to: " + end[1] + ".")
            end[0].append(disk)
        towers(n - 1, spare, start, end)

start = ([4, 3, 2, 1], "Start")
end = ([], "End")
spare = ([], "Spare")
towers(len(start[0]), start, spare, end)

print(start, spare, end)
