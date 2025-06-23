def read_file(fname: str) -> list:
    address = []
    with open(fname, "r", encoding="utf-8") as f:
        keys = f.readline().strip().split("\t")  # 첫 줄은 키로 사용
        for line in f:
            parts = line.strip().split("\t")
            values = []
            for part in parts:
                if part.startswith('"') and part.endswith('"'):
                    values.append(part.strip('"'))
                else:
                    values.append(part)
            if len(values) == len(keys):
                addr = dict(zip(keys, values))
                address.append(addr)
    return address

def insert_bst(tree: list, person: dict):
    if not tree:
        tree.append(person)
        return

    insert_recursively(tree, person)


def insert_recursively(tree: list, person: dict):
    if not tree:
        tree.append(person)
        return

    current = tree[0]

    if person['name'] < current['name']:
        # 왼쪽 서브트리 처리
        if len(tree) < 2:
            tree.append([])  # 왼쪽 서브트리 공간 생성
        if not isinstance(tree[1], list):
            tree[1] = []  # 안전하게 리스트로 지정
        insert_recursively(tree[1], person)

    else:
        # 오른쪽 서브트리 처리
        if len(tree) < 3:
            tree.append([])  # 오른쪽 서브트리 공간 생성
        if len(tree) == 2:  # 왼쪽 서브트리만 있을 경우
            tree.append([])
        if not isinstance(tree[2], list):
            tree[2] = []  # 안전하게 리스트로 지정
        insert_recursively(tree[2], person)

def inorder_bst(tree: list, result: list):
    if not tree:
        return
    if len(tree) > 1 and isinstance(tree[1], list):
        inorder_bst(tree[1], result)
    if tree:
        result.append(tree[0])
    if len(tree) > 2 and isinstance(tree[2], list):
        inorder_bst(tree[2], result)


def trace_specific_bst(tree: list, name: str):
    current = tree

    while current:
        if isinstance(current[0], dict) and 'name' in current[0]:
            print(current[0]['name'])  # 현재 노드의 이름을 한 줄에 출력

        if current[0]['name'] == name:
            return  # 찾으면 종료

        # 왼쪽으로 탐색
        if name < current[0]['name']:
            if len(current) > 1 and isinstance(current[1], list):
                current = current[1]
            else:
                break  # 왼쪽이 없으면 종료

        # 오른쪽으로 탐색
        else:
            if len(current) > 2 and isinstance(current[2], list):
                current = current[2]
            else:
                break  # 오른쪽이 없으면 종료

def delete_bst(tree: list, name: str):
    if not tree:
        print("Name not found in BST.")
        return tree

    # 삭제 대상 노드 탐색
    if name < tree[0]['name']:
        if len(tree) > 1 and isinstance(tree[1], list):
            tree[1] = delete_bst(tree[1], name)
    elif name > tree[0]['name']:
        if len(tree) > 2 and isinstance(tree[2], list):
            tree[2] = delete_bst(tree[2], name)
    else:
        # 삭제 대상 노드 찾음
        if len(tree) == 1:
            return []  # 리프 노드일 경우 직접 삭제

        if len(tree) == 2:
            return tree[1]  # 왼쪽 자식만 있을 경우 왼쪽 자식을 부모로 대체

        if len(tree) == 3:
            if not tree[2]:  # 오른쪽 자식이 없는 경우
                return tree[1]
            if not tree[1]:  # 왼쪽 자식이 없는 경우
                return tree[2]

            # 자식이 둘 다 있는 경우 (오른쪽 서브트리에서 최소값으로 교체)
            min_value = find_min(tree[2])
            tree[0] = min_value  # 현재 노드를 최소값으로 교체
            tree[2] = delete_bst(tree[2], min_value['name'])  # 최소값 노드 삭제

    return tree

def find_min(tree: list):
    current = tree
    while current and len(current) > 1 and isinstance(current[1], list):
        current = current[1]
    return current[0] if current else None



def save_bst_to_file(tree: list, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        result = []
        inorder_bst(tree, result)  # BST 중위 순회로 정렬된 결과

        if result:
            keys = result[0].keys()
            f.write("\t".join(keys) + "\n")  # 첫 줄: 헤더
            for addr in result:
                values = [str(addr[key]) for key in keys]
                f.write("\t".join(values) + "\n")
        else:
            print("No data to save.")

if __name__ == "__main__":
    bst_tree = [] # inorder를 위한 트리
    all_address = [] # 전체 학생을 저장하는 리스트
    while (cmd := input("$ ")) and cmd != "exit":
        command = cmd.split()[0]
        if "read" == command:
            address = read_file(cmd.split()[1])
            for addr in address:
                insert_bst(bst_tree, addr)
                all_address.append(addr)
        elif "list" == command:
            result = []
            inorder_bst(bst_tree, result)
            for addr in result:
                for k, v in addr.items():
                    if k == "name":
                        print(v)
                    else:
                        print(f"\t{k}: {v}")
        elif "find" == command:
            name = cmd.split()[1]
            for addr in all_address:
                for k, v in addr.items():
                    if v == name:
                        for a,b in addr.items():
                            if a == 'name':
                                print(name)
                            else:
                                print(f"\t{a}: {b}")
        elif "add" == command:
            name = cmd.split()[1]
            is_exist = False
            for addr in all_address:
                for k, v in addr.items():
                    if v == name:
                        is_exist = True
                        break

            new_addr = dict()
            keys = ['company_name', 'address', 'zip', 'phone', 'email']
            if not is_exist:
                new_addr['name'] = name
                for key in keys:
                    new_value = input(f"{key}? ")
                    new_addr[key] = new_value
                insert_bst(bst_tree, new_addr)
                all_address.append(new_addr)
                print(f'{name} was successfully added.')
        elif "trace" == command:
            name = cmd.split()[1]
            trace_specific_bst(bst_tree, name)
        elif "delete" == command:
            name = cmd.split()[1]
            bst_tree = delete_bst(bst_tree, name)
        elif "save" == command:
            filename = cmd.split()[1]
            save_bst_to_file(bst_tree, filename)

# read address_book.tsv