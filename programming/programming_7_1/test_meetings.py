from unittest import TestCase
from Ponomarenko_pmi25.programming.programming_7_1.meetings import Meetings, MeetingError
from Ponomarenko_pmi25.programming.programming_7_1.online_meeting import OnlineMeeting
from Ponomarenko_pmi25.programming.programming_7_1.memento import Creator, Caretaker, copy_of_meetings, memento


class Test(TestCase):

    a = '11 19.10.2020 18:00 20:00 http://aoom/49839gk483 Maria Austin Ernest Hemingway'
    b1 = '12 20.10.2020 19:00 21:00 http://zoom/49839gk483 Genry Mayers Roza Guns'
    c = '13 20.10.2020 19:00 21:00 http://zoom/49839gk483 Genry Mayers Roza Guns'
    d = '14 20.10.2020 19:00 21:00 http://zoom/49839gk483 Genry Mayers Roza Guns'
    d_change = '14 20.10.2020 16:00 21:00 http://zoom/49839gk483 Genry Mayers Roza Guns'
    wrong_obj = '14 19.1$0.2020 18:00 20:00 http://aoom/49839gk483 Maria Austin Ernest Hemingway'


    @classmethod
    def setUp(cls) -> None:
        cls.test_list = Meetings()
        cls.test_list.add_to_list(OnlineMeeting(cls.b1.split()))
        cls.test_list.add_to_list(OnlineMeeting(cls.a.split()))
        cls.originator = Creator(cls.test_list)
        cls.caretaker = Caretaker(cls.originator)

    def test_exist_in_list(self):
        self.assertTrue(self.test_list.exist_in_list(OnlineMeeting(self.a.split())))
        self.assertFalse(self.test_list.exist_in_list(OnlineMeeting(self.c.split())))

    def test_add(self):
        self.test_list.add(self.c, None, 'test')
        self.assertTrue(self.test_list.exist_in_list(OnlineMeeting(self.c.split())))
        self.assertRaises(MeetingError, lambda: self.test_list.add(self.wrong_obj, None, 'test'))

    def test_remove_from_list(self):
        self.test_list.remove_from_list('12')
        r = Meetings()
        r.add_to_list(OnlineMeeting(self.a.split()))
        self.assertListEqual(self.test_list.meetings, r.meetings)
        self.test_list.remove_from_list('14')
        self.assertListEqual(self.test_list.meetings, r.meetings)

    def test_sort(self):
        expected = Meetings()
        expected.add_to_list(OnlineMeeting(self.a.split()))
        expected.add_to_list(OnlineMeeting(self.b1.split()))
        self.test_list.sort('id')
        self.assertListEqual(expected.meetings, self.test_list.meetings)
        self.test_list.sort('owner')
        self.assertFalse(expected.meetings == self.test_list.meetings)

    def test_search_in_list(self):
        expected = self.test_list.meetings
        actual = self.test_list.search_in_list('00')
        self.assertListEqual(expected, actual)
        actual1 = self.test_list.search_in_list('aoo')
        self.assertFalse(expected == actual1)

    def test_rewrite_file(self, s='input.txt'):
        self.assertRaises(FileExistsError, self.test_list.rewrite_file, 'qqq.txt')
        self.test_list.add_to_list(OnlineMeeting(self.d.split()))
        self.test_list.rewrite_file(s)
        f = open(s, 'r')
        l = f.readlines()
        f.close()
        self.assertTrue(len(l) == 3)

    def test_fill_list_from_file(self):
        self.assertRaises(FileExistsError, self.test_list.rewrite_file, 'qqq.txt')
        result = Meetings()
        result.fill_list_from_file('input.txt')
        self.assertTrue(len(result.meetings) == 3)

    def test_edit(self):
        expected = Meetings()
        expected.add_to_list(OnlineMeeting(self.d_change.split()))
        expected.add_to_list(OnlineMeeting(self.a.split()))

        expected1 = Meetings()
        expected1.add_to_list(OnlineMeeting(self.d.split()))
        expected1.add_to_list(OnlineMeeting(self.a.split()))
        expected1.edit(self.d_change, None, '14', 'test')
        self.assertListEqual(expected.meetings, expected1.meetings)
        self.assertRaises(MeetingError, self.test_list.edit, self.wrong_obj, None, '14', 'test')

    def test_memento(self):
        ls1 = copy_of_meetings(self.test_list)
        ls1.add_to_list(self.c)
        self.test_list = memento(ls1, self.originator, self.caretaker)
        self.assertTrue(self.caretaker.id == 0)
        self.assertTrue(self.originator.get_condition_o().get_size() == 3)

        ls1 = copy_of_meetings(self.test_list)
        ls1.add_to_list(self.d)
        self.test_list = memento(ls1, self.originator, self.caretaker)
        self.assertTrue(self.caretaker.id == 1)
        self.assertTrue(self.originator.get_condition_o().get_size() == 4)

        self.caretaker.undo_redo('undo')
        self.assertTrue(self.originator.get_condition_o().get_size() == 3)

        self.caretaker.undo_redo('redo')
        self.assertTrue(self.originator.get_condition_o().get_size() == 4)





