from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_cannot_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_with_long_name_not_added(self):
        collector = BooksCollector()
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы'])
    def test_set_book_genre_sets_correctly(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', genre)
        assert collector.get_book_genre('Книга 2') == genre

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Комедии')
        collector.set_book_genre('Книга 2', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга 1']

    def test_get_books_for_children_excludes_aged_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Книга 2']

    def test_add_book_in_favorites_adds_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert sorted(collector.get_list_of_favorites_books()) == ['Книга 1', 'Книга 2']

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.books_genre['Книга 1'] = 'Фантастика'
        assert collector.get_book_genre('Книга 1') == 'Фантастика'

    def test_get_book_genre_returns_none_for_unknown_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_genre_returns_correct_dictionary(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Комедии'
        }
        assert collector.get_books_genre() == {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Комедии'
        }

    def test_get_books_genre_returns_empty_dict_initially(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}