from manim import *
from manim_slides import Slide
import numpy as np

my_template = TexTemplate()
my_template.add_to_preamble(r"\usepackage{polski}")
my_template.add_to_preamble(r"\usepackage{physics}")
my_template.add_to_preamble(r"\usepackage{amsmath}")
my_template.add_to_preamble(r"\DeclareMathOperator{\cov}{cov}")
my_template.add_to_preamble(r"\let\var\relax")
my_template.add_to_preamble(r"\DeclareMathOperator{\var}{var}")

class Final1_3(Slide):
    def construct(self):

        # ==========================================================
        # Slajd 1: Wyprowadzenie Wzoru
        # ==========================================================
        slide2_title = Text("Wyprowadzenie Wzoru", font_size=60, weight=BOLD)
        slide2_subtitle = Text("Konstrukcja danych, założenia i dowód", font_size=36)
        slide2_subtitle.next_to(slide2_title, DOWN, buff=0.5)

        self.play(FadeIn(slide2_title, scale=0.5))
        self.play(Write(slide2_subtitle))
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 2: Legenda Symboli Matematycznych
        # ==========================================================
        header = Text("Legenda Symboli Matematycznych", font_size=40, color=BLUE).to_edge(UP)

        item1 = Tex(r"$\bullet$ Macierz A transponowana: \quad $A^T$", tex_template=my_template, font_size=36)
        item2 = Tex(r"$\bullet$ Iloczyn skalarny/wewn.: \quad $x \cdot y = \langle x, y \rangle = x^Ty$", tex_template=my_template, font_size=36)
        item3 = Tex(r"$\bullet$ Długość/norma wektora: \quad $\| x \|$", tex_template=my_template, font_size=36)
        item4 = Tex(r"$\bullet$ Kowariancja zmiennych X i Y: \quad $\cov(X, Y)$", tex_template=my_template, font_size=36)
        item5 = Tex(r"$\bullet$ Wariancja zmiennej X: \quad $\var(X) = \cov(X,X\text{ )}  $", tex_template=my_template, font_size=36)

        legend = VGroup(item1, item2, item3, item4, item5).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.next_to(header, DOWN, buff=1).align_to(header, LEFT)

        self.play(Write(header))
        for item in legend:
            self.play(FadeIn(item, shift=RIGHT))
            self.next_slide()
                
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 3: Konstrukcja Macierzy Danych
        # ==========================================================
        header = Text("Konstrukcja Macierzy Danych", font_size=40, color=BLUE).to_edge(UP)
        
        desc = Tex(
            r"Na początku zdefiniujemy, jak wyglądają nasze dane. Wektory $X_i$,\\",
            r"o wymiarach $d\times 1$, reprezentują obserwacje o d cechach.\\",
            r"Natomiast $\mathbb{X}$ ($n\times d$) jest tablicą składającą się z\\",
            r"transponowanych wektorów $X_i$.",
            tex_template=my_template,
            font_size=32
        ).next_to(header, DOWN, buff=0.5)

        matrices = MathTex(
            r"X_i = \begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_d \end{bmatrix}",
            r"\quad\quad\quad",
            r"\mathbb{X} = \begin{bmatrix} \text{---} & X_1^T & \text{---}\\ \text{---} &X_2^T& \text{---}\\ &\vdots&\\ \text{---} &X_n^T& \text{---} \end{bmatrix}",
            tex_template=my_template,
            font_size=40
        ).next_to(desc, DOWN, buff=1)

        self.play(Write(header))
        self.play(Write(desc))
        self.play(Write(matrices))
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 4: Wizualizacja Głównych Składowych w 2D
        # ==========================================================
        header = Text("Wizualizacja Głównych Składowych w 2D", font_size=40, color=BLUE).to_edge(UP)
        self.add(header)
        
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6).shift(DOWN*0.5)
        
        np.random.seed(42)
        x_vals = np.random.normal(0, 1, 40)
        y_vals = 0.8 * x_vals + np.random.normal(0, 0.3, 40)
        dots = VGroup(*[Dot(axes.c2p(x, y), color=LIGHT_GREY) for x, y in zip(x_vals, y_vals)])
        
        pc1 = Arrow(axes.c2p(0,0), axes.c2p(1.5, 1.2), buff=0, color=RED, stroke_width=6)
        pc2 = Arrow(axes.c2p(0,0), axes.c2p(-0.6, 0.75), buff=0, color=GREEN, stroke_width=6)
        
        self.play(Create(axes), run_time=3)
        self.play(FadeIn(dots, lag_ratio=0.1), run_time=3)
        self.play(GrowArrow(pc1), GrowArrow(pc2), run_time=3)
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 5: Rzut Prostokątny
        # ==========================================================
        header = Text("Rzut Prostokątny", font_size=40, color=BLUE).to_edge(UP)
        self.add(header)

        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        origin = np.array([0.0, 0.0, 0.0])
        xi_pos = np.array([2.0, 4.0, 0.0])

        dir_vec = np.array([5.0, 2.0, 0.0])
        w_norm = dir_vec / np.linalg.norm(dir_vec)

        axis_line = DashedLine(w_norm * -3, w_norm * 8, color=LIGHT_GREY)
        
        arrow_w = Arrow(origin, dir_vec, buff=0, color=BLUE)
        label_w = MathTex("w", color=BLUE).next_to(arrow_w.get_end(), DOWN+RIGHT, buff=0.1)

        arrow_xi = Arrow(origin, xi_pos, buff=0, color=RED_C)
        dot_xi = Dot(xi_pos, color=RED)
        label_xi = MathTex("x_i", color=RED).next_to(dot_xi, UP)

        proj_scalar = np.dot(xi_pos, w_norm)
        proj_pos = proj_scalar * w_norm

        dashed_proj = DashedLine(xi_pos, proj_pos, color=WHITE)

        right_angle = RightAngle(
            Line(proj_pos, xi_pos), 
            Line(proj_pos, origin),
            length=0.3, 
            color=WHITE
        )

        arrow_zi = Arrow(origin, proj_pos, buff=0, color=GREEN, stroke_width=8, max_tip_length_to_length_ratio=0.15)
        dot_proj = Dot(proj_pos, color=GREEN)
        label_zi = MathTex("z_i", color=GREEN).next_to(dot_proj, DOWN+RIGHT, buff=0.2)

        visual_group = VGroup(
            plane, 
            axis_line, arrow_w, label_w, 
            arrow_xi, dot_xi, label_xi, 
            dashed_proj, right_angle, 
            arrow_zi, dot_proj, label_zi
        )

        visual_group.shift(DOWN * 1.7 + LEFT * 2)

        eq1 = MathTex(r"\|w\| = 1")
        eq2 = MathTex(r"z_i = \langle X_i, w \rangle w = (X_i^T w) w")
        eqs = VGroup(eq1, eq2).arrange(DOWN, buff=0.3).to_edge(DOWN)
        
        eqs_bg = BackgroundRectangle(eqs, color=BLACK, fill_opacity=0.8)

        self.play(Create(plane), run_time=1.5) 
        self.play(Create(axis_line), run_time=1.5)
        self.play(GrowArrow(arrow_w), Write(label_w), run_time=3.0)
        self.play(GrowArrow(arrow_xi), FadeIn(dot_xi), Write(label_xi), run_time=3.0)
        self.play(Create(dashed_proj), Create(right_angle), run_time=3.0)
        self.play(GrowArrow(arrow_zi), FadeIn(dot_proj), Write(label_zi), run_time=3.0)
        self.play(FadeIn(eqs_bg), Write(eqs), run_time=3.0)
        self.wait(2)
        self.next_slide()
        self.clear()
        # ==========================================================
        # Slajd 6: Konstrukcja Macierzy Kowariancji 1
        # ==========================================================
        header = Text("Konstrukcja Macierzy Kowariancji", font_size=40, color=BLUE).to_edge(UP)
        self.add(header)

        eq1 = MathTex(r"\text{Wzór na kowariancję: } \cov(X, Y) = \frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})", tex_template=my_template, font_size=36)
        
        text1 = Tex(
            r"W dalszej części zakładamy, że zmienne są wyśrodkowane\\",
            r"względem swoich średnich ($\bar{x} = \bar{y} = 0$).\\",
            r"Wtedy w naszej macierzy $\mathbb{X}$, kowariancję j-tej i k-tej\\",
            r"zmiennej możemy zapisać w postaci",
            tex_template=my_template, font_size=32
        )
        
        eq2 = MathTex(r"\cov(j ,k) = \frac{1}{n} \sum_{i=0}^{n} x_{ij}x_{ik}", tex_template=my_template, font_size=36)
        
        text2 = Tex(r"Gdzie elemnt $x_{ij}$ jest i-tą obserwacją j-tej zmiennej", tex_template=my_template, font_size=32)

        content = VGroup(eq1, text1, eq2, text2).arrange(DOWN, buff=0.5).next_to(header, DOWN, buff=0.5)

        self.play(Write(eq1))
        self.next_slide()
        self.play(FadeIn(text1))
        self.next_slide()
        self.play(Write(eq2))
        self.play(FadeIn(text2))
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 7: Konstrukcja Macierzy Kowariancji 2
        # ==========================================================
        header = Text("Konstrukcja Macierzy Kowariancji", font_size=40, color=BLUE).to_edge(UP)
        self.add(header)

        t1 = Tex(r"Przyjrzyjmy się teraz macierzy", tex_template=my_template, font_size=32)
        eq1 = MathTex(r"M = \mathbb{X}^T \mathbb{X}", tex_template=my_template, font_size=36)
        
        t2 = Tex(
            r"a konkretnie elementowi znajdującemu się w j-tym wierszu\\",
            r"i k-tej kolumnie, który oznaczymy jako $M_{jk}$. Ze wzoru\\",
            r"na mnożenie macierzy wiemy, że jest to iloczyn skalarny\\",
            r"k-tej kolumny $\mathbb{X}$ oraz j-tego wiersza $\mathbb{X}^T$,\\",
            r"czyli j-tej kolumny $\mathbb{X}$. Dzięki temu otrzymujemy",
            tex_template=my_template, font_size=32
        )
        
        eq2 = MathTex(r"M_{jk} = x_{1j}x_{1k} + x_{2j}x_{2k} + \cdots + x_{nj}x_{nk} = \sum_{i=0}^{n} x_{ij}x_{ik} = n\cov(j, k)", tex_template=my_template, font_size=36)
        t3 = Tex(r"Łatwo wtedy zauważyć, że macierz kowariancji $S$, to", tex_template=my_template, font_size=32)
        eq3 = MathTex(r"S = \frac{1}{n} M = \frac{1}{n} \mathbb{X}^T \mathbb{X}", tex_template=my_template, font_size=36)

        content = VGroup(t1, eq1, t2, eq2, t3, eq3).arrange(DOWN, buff=0.3).next_to(header, DOWN, buff=0.3)

        for item in content:
            self.play(FadeIn(item, shift=UP*0.1))
            self.next_slide()
            
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 9: Cel i Założenia
        # ==========================================================
        header = Text("Cel i Założenia", font_size=48, color=BLUE).to_edge(UP)
        self.add(header)

        zalozenia_title = Tex(r"\textbf{Założenia:}", tex_template=my_template, font_size=40)
        zalozenia_subtitle = Tex(r"Zbiór danych jest:", tex_template=my_template, font_size=36)

        item_1 = Tex(r"1. wyśrodkowany: $\overline{X_i}=0$", tex_template=my_template, font_size=36)
        item_2 = Tex(r"2. znormalizowany: wartości w przedziale $[0, 1]$", tex_template=my_template, font_size=36)

        list_items = VGroup(item_1, item_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        zalozenia_group = VGroup(
            zalozenia_title, 
            zalozenia_subtitle, 
            list_items
        ).arrange(DOWN, buff=0.4)

        cel = Tex(
            r"\textbf{Cel: }znalezienie wektora $\|w\|=1$,\\",
            r"który maksymalizuje wariancję.",
            tex_template=my_template, font_size=40
        )

        content = VGroup(zalozenia_group, cel).arrange(DOWN, buff=1.2).center()

        self.next_slide()
        self.play(Write(zalozenia_title), Write(zalozenia_subtitle))
        self.next_slide()
        self.play(FadeIn(item_1, shift=RIGHT * 0.5))
        self.next_slide()
        self.play(FadeIn(item_2, shift=RIGHT * 0.5))

        self.next_slide()
        self.play(FadeIn(cel, scale=1.1))
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 8: Obliczanie Wariancji
        # ==========================================================
        header = Text("Obliczanie Wariancji", font_size=40, color=BLUE).to_edge(UP)
        self.add(header)

        t1 = Tex(r"Niech $Z = [z_1, z_2, \ldots, z_n]^T$, będzie rzutem ortogonalnym\\ danych na wektor $w$. Wtedy", tex_template=my_template, font_size=32)
        
        eq1 = MathTex(
            r"\var(Z) &= \frac{1}{n}\sum_{i=1}^{n}(z_i)^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i^T w)^2 = \frac{1}{n} (\mathbb{X}w)^T\mathbb{X}w \\",
            r"&= w^T\left( \frac{1}{n} \mathbb{X}^T \mathbb{X} \right) w = w^T S w",
            tex_template=my_template, font_size=40
        )

        content = VGroup(t1, eq1).arrange(DOWN, buff=0.7).center()

        self.play(Write(t1))
        self.next_slide()
        self.play(Write(eq1))
        
        self.next_slide()
        self.clear()

        # ==========================================================
        # Slajd 9: Optymalizacja z Użyciem Mnożników Lagrange'a
        # ==========================================================
        header = Text("Optymalizacja z Użyciem Mnożników Lagrange'a", font_size=36, color=BLUE).to_edge(UP)
        self.add(header)

        t1 = Tex(r"Naszym celem jest zmaksymalizowanie wariancji, $\var(Z) = w^TSw$,\\ z ograniczeniem $\|w\| = 1 \implies w^Tw = 1$.", tex_template=my_template, font_size=32)
        
        eq1 = MathTex(r"\pdv{(w^TSw)}{w} = \lambda \pdv{(w^Tw - 1)}{w}", tex_template=my_template, font_size=40)
        eq2 = MathTex(r"2Sw = 2\lambda w \implies Sw=\lambda w", tex_template=my_template, font_size=40)
        
        t2 = Tex(r"Czyli $w$, jest wektorem własnym macierzy $S$. Pondato", tex_template=my_template, font_size=32)
        eq3 = MathTex(r"w^TSw = w^T\lambda w = \lambda", tex_template=my_template, font_size=40)
        t3 = Tex(r"czyli jest to dokładnie wektor odpowiadający największe wartości własnej.", tex_template=my_template, font_size=32)

        content = VGroup(t1, eq1, eq2, t2, eq3, t3).arrange(DOWN, buff=0.4).next_to(header, DOWN, buff=0.3)

        for step in content:
            self.play(FadeIn(step, shift=UP*0.2))
            self.next_slide()

if __name__ == "__main__":
    scene = Final1_3()
    scene.render()