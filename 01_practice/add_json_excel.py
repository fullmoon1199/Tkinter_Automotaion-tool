def add_node(self):
        with open('F:\\tkinter\\01_practice\\sample2.json') as file:
            datas = json.load(file)
            linux_feature = list(datas['Linux'].keys())
            android_feature = list(datas['Android'].keys())
            la_feature = list(datas['LinuxAndroid'].keys())
        # Configure the CheckboxTreeview to use the scrollbar

        parent_id = ""
        #insert root node
        Linux = str(1)
        Android = str(2)
        LA = str(3)
        #tree node insert
        self.tree.insert(parent_id, "end", Linux, text='Linux')
        self.tree.insert(parent_id, "end", Android, text='Android')
        self.tree.insert(parent_id, "end", LA, text='LinuxAndroid')
        self.tree2.insert(parent_id, "end", Linux, text='Linux')
        self.tree2.insert(parent_id, "end", Android, text='Android')
        self.tree2.insert(parent_id, "end", LA, text='LinuxAndroid')
        #하위 nood insert
        for i in range(0, linux_feature.__len__()):
            node_id = f"{i}1"
            self.tree.insert(Linux, "end", node_id, text=linux_feature[i])
            self.tree2.insert(Linux, "end", node_id, text=linux_feature[i])
            sublist = datas['Linux'][linux_feature[i]]
            json_test = [feature['name'] for feature in sublist]
            for j in range(json_test.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id, "end", f"{i}2_{j}", text=json_test[j])
                    self.auto += 1
                else:
                    self.tree2.insert(node_id, "end", f"{i}2_{j}", text=json_test[j])
                    self.manual += 1
        for i in range(0, android_feature.__len__()):
            node_id2 = f"{i}2"
            self.tree.insert(Android, "end", node_id2, text=android_feature[i])
            self.tree2.insert(Android, "end", node_id2, text=android_feature[i])
            sublist2 = datas['Android'][android_feature[i]]
            json_test2 = [feature['name'] for feature in sublist2]
            for j in range(json_test2.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id2, "end", f"{i}3_{j}", text=json_test2[j])
                    self.auto += 1
                else:
                    self.tree2.insert(node_id2, "end", f"{i}3_{j}", text=json_test2[j])
                    self.manual += 1
        
        for i in range(0, la_feature.__len__()):
            node_id3 = f"{i}3"
            self.tree.insert(LA, "end", node_id3, text=la_feature[i])
            self.tree2.insert(LA, "end", node_id3, text=la_feature[i])
            sublist3 = datas['LinuxAndroid'][la_feature[i]]
            json_test3 = [feature['name'] for feature in sublist3]
            
            for j in range(json_test3.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id3, "end", f"{i}4_{j}", text=json_test3[j])
                    self.auto += 1
                else:
                    self.tree2.insert(node_id3, "end", f"{i}4_{j}", text=json_test3[j])
                    self.manual += 1