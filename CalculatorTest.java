import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    void testAddition() {
        assertEquals(8, calc.add(5, 3));   // Pass
        assertNotEquals(9, calc.add(4, 4)); // Pass
    }

    @Test
    void testIsEven() {
        assertTrue(calc.isEven(6));        // Pass
        assertFalse(calc.isEven(5));       // Pass
    }
}
