def solution(files) :
    import re
    def parse_file(file, index) :
        match = re.match(r'([^\d]+)(\d{1,5})', file)
        head, number = match.group(1), match.group(2)
        return (head.lower(), int(number), index, file)

    parsed = [parse_file(file, idx) for idx, file in enumerate(files)]
    sorted_files = sorted(parsed, key=lambda x: (x[0], x[1], x[2]))
    
    return [file[3] for file in sorted_files]
