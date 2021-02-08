class TimeThis:
    def __init__(self, event_name=None):
        self.event_name = event_name

    def start(self):
        self.start_time = time.time()

    def end(self):
        end_time = time.time()
        event_time = round(end_time - self.start_time, 2)
        if self.event_name is not None:
            st.write(f'{self.event_name} execution time = {event_time}s')
        else:
            st.write(f'execution time = {event_time}s')