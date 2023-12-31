# testy


## Struktura Systemu lub Aplikacji

Projekt składa się z następujących elementów:
- Plik `main.py`: Główny plik zawierający implementację klas `HulajnogaElektryczna`, `Hulajnoga5km`, `Hulajnoga10km`, `Hulajnoga15km` oraz `FabrykaHulajnog`. Zawiera również kod do interakcji z użytkownikiem w pętli while.
- Pliki testowe: `test_a.py`, `test_b.py`, `test_c.py` zawierające testy jednostkowe, integracyjne i akceptacyjne.

## Scenariusze Testów

1. Testy jednostkowe:
   - Sprawdzenie poprawności wyświetlania informacji dla każdego rodzaju hulajnogi.
   - Sprawdzenie poprawności tworzenia hulajnóg różnych typów i dodawania ich do fabryki.
   - Sprawdzenie tworzenia hulajnogi z nieznanym typem.

2. Testy integracyjne:
   - Sprawdzenie poprawności tworzenia hulajnóg różnych typów i dodawania ich do fabryki.

3. Testy akceptacyjne:
   - Sprawdzenie poprawności wyświetlania informacji dla hulajnogi.
   - Sprawdzenie dodawania produktu do fabryki.

## Wykorzystane Narzędzia i Biblioteki

- Python 3.8: Język programowania wykorzystany do implementacji aplikacji.
- Unittest: Moduł do tworzenia i wykonywania testów jednostkowych.
- Pytest: Biblioteka do testowania jednostkowego i integracyjnego.


## Ewentualne Problemy i Ich Rozwiązania

1. Problem: Tworzenie hulajnogi z nieznanym typem.
   Rozwiązanie: Dodanie obsługi nieznanego typu w metodzie `utworz_hulajnoge` klasy `FabrykaHulajnog`. W przypadku nieznanego typu, zwracana jest wartość None i wypisywany jest odpowiedni komunikat.
