test_add_new_book_add_two_books

Проверяет, что можно добавить две разные книги, и они корректно сохраняются в словарь books_genre.

test_add_new_book_cannot_add_duplicate

Проверка, что нельзя добавить одну и ту же книгу дважды. После попытки дублирования в словаре остаётся только одна запись.

test_add_new_book_with_long_name_not_added

Проверяет ограничение на длину названия книги. Книга с именем длиннее 40 символов не добавляется.

test_set_book_genre_sets_correctly

Проверяется, что метод set_book_genre устанавливает допустимые жанры корректно.

test_get_books_with_specific_genre_returns_correct_books

Проверяется, что метод get_books_with_specific_genre возвращает книги только указанного жанра.

test_get_books_for_children_excludes_aged_genres

Проверка, что метод get_books_for_children исключает книги с жанрами, содержащими возрастной рейтинг.

test_add_book_in_favorites_adds_only_once

Проверяет, что одну и ту же книгу можно добавить в избранное только один раз.

test_delete_book_from_favorites_removes_book

Проверяет корректность удаления книги из избранного списка.

test_get_list_of_favorites_books_returns_correct_list

Проверка, что метод get_list_of_favorites_books возвращает правильный список избранных книг.

test_get_book_genre_returns_correct_genre
Проверяет, что метод get_book_genre возвращает корректный жанр для книги, если она присутствует в словаре books_genre.

test_get_book_genre_returns_none_for_unknown_book
Проверяет, что метод get_book_genre возвращает None, если книга отсутствует в словаре books_genre.

test_get_books_genre_returns_correct_dictionary
Проверяет, что метод get_books_genre возвращает точное содержимое словаря books_genre.

test_get_books_genre_returns_empty_dict_initially
Проверяет, что при создании нового экземпляра класса словарь books_genre изначально пуст.
