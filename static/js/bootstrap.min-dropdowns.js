/*!
 * Bootstrap v3.3.4 (http://getbootstrap.com)
 * Copyright 2011-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
*/

// BOOTSTRAP PORTION:
+(function (a) {
	"use strict";
	function b(b) {
		(b && 3 === b.which) ||
			(a(e).remove(),
			a(f).each(function () {
				var d = a(this),
					e = c(d),
					f = { relatedTarget: this };
				e.hasClass("open") &&
					(e.trigger((b = a.Event("hide.bs.dropdown", f))),
					b.isDefaultPrevented() ||
						(d.attr("aria-expanded", "false"),
						e.removeClass("open").trigger("hidden.bs.dropdown", f)));
			}));
	}
	function c(b) {
		var c = b.attr("data-target");
		c ||
			((c = b.attr("href")),
			(c = c && /#[A-Za-z]/.test(c) && c.replace(/.*(?=#[^\s]*$)/, "")));
		var d = c && a(c);
		return d && d.length ? d : b.parent();
	}
	function d(b) {
		return this.each(function () {
			var c = a(this),
				d = c.data("bs.dropdown");
			d || c.data("bs.dropdown", (d = new g(this))),
				"string" == typeof b && d[b].call(c);
		});
	}
	var e = ".dropdown-backdrop",
		f = '[data-toggle="dropdown"]',
		g = function (b) {
			a(b).on("click.bs.dropdown", this.toggle);
		};
	(g.VERSION = "3.3.4"),
		(g.prototype.toggle = function (d) {
			var e = a(this);
			if (!e.is(".disabled, :disabled")) {
				var f = c(e),
					g = f.hasClass("open");
				if ((b(), !g)) {
					"ontouchstart" in document.documentElement &&
						!f.closest(".navbar-nav").length &&
						a('<div class="dropdown-backdrop"/>')
							.insertAfter(a(this))
							.on("click", b);
					var h = { relatedTarget: this };
					if (
						(f.trigger((d = a.Event("show.bs.dropdown", h))),
						d.isDefaultPrevented())
					)
						return;
					e.trigger("focus").attr("aria-expanded", "true"),
						f.toggleClass("open").trigger("shown.bs.dropdown", h);
				}
				return !1;
			}
		}),
		(g.prototype.keydown = function (b) {
			if (
				/(38|40|27|32)/.test(b.which) &&
				!/input|textarea/i.test(b.target.tagName)
			) {
				var d = a(this);
				if (
					(b.preventDefault(),
					b.stopPropagation(),
					!d.is(".disabled, :disabled"))
				) {
					var e = c(d),
						g = e.hasClass("open");
					if ((!g && 27 != b.which) || (g && 27 == b.which))
						return (
							27 == b.which && e.find(f).trigger("focus"), d.trigger("click")
						);
					var h = " li:not(.disabled):visible a",
						i = e.find('[role="menu"]' + h + ', [role="listbox"]' + h);
					if (i.length) {
						var j = i.index(b.target);
						38 == b.which && j > 0 && j--,
							40 == b.which && j < i.length - 1 && j++,
							~j || (j = 0),
							i.eq(j).trigger("focus");
					}
				}
			}
		});
	var h = a.fn.dropdown;
	(a.fn.dropdown = d),
		(a.fn.dropdown.Constructor = g),
		(a.fn.dropdown.noConflict = function () {
			return (a.fn.dropdown = h), this;
		}),
		a(document)
			.on("click.bs.dropdown.data-api", b)
			.on("click.bs.dropdown.data-api", ".dropdown form", function (a) {
				a.stopPropagation();
			})
			.on("click.bs.dropdown.data-api", f, g.prototype.toggle)
			.on("keydown.bs.dropdown.data-api", f, g.prototype.keydown)
			.on("keydown.bs.dropdown.data-api", '[role="menu"]', g.prototype.keydown)
			.on(
				"keydown.bs.dropdown.data-api",
				'[role="listbox"]',
				g.prototype.keydown
			);
})(jQuery),

function f() {
  g
    .removeClass("active")
    .find("> .dropdown-menu > .active")
    .removeClass("active")
    .end()
    .find('[data-toggle="tab"]')
    .attr("aria-expanded", !1),
    b
      .addClass("active")
      .find('[data-toggle="tab"]')
      .attr("aria-expanded", !0),
    h ? (b[0].offsetWidth, b.addClass("in")) : b.removeClass("fade"),
    b.parent(".dropdown-menu").length &&
      b
        .closest("li.dropdown")
        .addClass("active")
        .end()
        .find('[data-toggle="tab"]')
        .attr("aria-expanded", !0),
    e && e();
};

// MY CODE:
$(document).ready(function () {
	$("#id_available_days").multiselect({
		includeSelectAllOption: true,
	});
});
