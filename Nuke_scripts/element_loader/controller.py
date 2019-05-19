class ElementLoaderController(object):
    def __init__(self, view, model):
        super(ElementLoaderController, self).__init__()
        self.view = view
        self.model = model
        self.connect_signal_slot()
        # self.update_task()
        # self.update_version()

    def connect_signal_slot(self):
        self.view.sequence_list.currentIndexChanged.connect(self.update_shot_list)
        self.view.shot_list.currentIndexChanged.connect(self.update_task)
        print "run,,,"

    def set_context(self):
        if self.model.match:
            self.view.set_project(self.model.info['project'])
            sequences = self.model.search_sequences()
            self.view.set_sequence(sequences)
            if self.model.info['sequence'] in sequences:
                self.view.sequence_list.setCurrentIndex(sequences.index(self.model.info['sequence']))
            sequence = str(self.view.sequence_list.currentText())
            shots = self.model.search_shots(sequence)
            # print "shots:",shots
            self.view.set_shot(shots)
            if self.model.info['shot'] in shots:
                self.view.shot_list.setCurrentIndex(shots.index(self.model.info['shot']))


    def update_shot_list(self):
        sequence = self.view.sequence_list.currentText()
        shots = self.model.search_shots(sequence)
        if len(shots) == 0:
            self.view.clear_table()
            self.view.set_shot(shots)
        else:
            self.view.set_shot(shots)

    def update_task(self):
        sequence = self.view.sequence_list.currentText()
        shot = self.view.shot_list.currentText()
        if len(sequence) and len(shot) != 0:
            tasks = self.model.search_task(sequence, shot)
            self.view.clear_table()
            row_count = 0
            for task in tasks:
                print "row_count:",row_count
                print "task:",task
                versions = self.model.search_versions(sequence, shot, task)
                print "versions:",versions
                self.view.set_task(row_count, task)
                # version = self.view.version_combo.currentText()
                # print "version:",version
                # format_list = self.model.search_resolution(sequence, shot, task, version)
                if len(versions) == 0:
                    versions = ['No version']
                self.view.set_version(row_count,versions,task,sequence,shot)

                row_count += 1

    # def update_format(self,info):
    #     print "update_formate is run...."
    #     sequence = self.view.sequence_list.currentText()
    #     shot = self.view.shot_list.currentText()
    #     tasks = self.model.search_task(sequence, shot)
    #     for task in tasks:
    #         version = self.view.version_combo.currentText()
    #         format_list = self.model.search_resolution(sequence,shot,task,version)
    #         self.view.set_resolution(row=info['row'],resolutions=format_list)


            # for task in tasks:
            #     versions = self.model.search_versions(sequence,shot,task)
            #     print "versions:",versions
            #     self.view.set_version(row_count,versions)
            #     row_count += 1




