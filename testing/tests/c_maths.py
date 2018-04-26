# -*- coding: utf8 -*-
########################################################################################
# This file is part of exhale.  Copyright (c) 2017-2018, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################

"""
Tests for the ``c_maths`` project.
"""

from __future__ import unicode_literals
import os

from testing.base import ExhaleTestCase
from testing.decorators import confoverrides, no_run
from testing.hierarchies import *


class CMathsTests(ExhaleTestCase):
    """
    Primary test class for project ``c_maths``.
    """

    test_project = "c_maths"
    """
    Index into ``testing/projects``.

    See also: :data:`testing.base.ExhaleTestCase.test_project`.
    """

    def test_app(self):
        """Simply checks :func:`testing.base.ExhaleTestCase.checkRequiredConfigs`."""
        self.checkRequiredConfigs()

    @confoverrides(exhale_args={"containmentFolder": "./alt_api"})
    def test_alt_out(self):
        """
        Test ``"./alt_api"`` rather than default ``"./api"`` as ``"containmentFolder"``.
        """
        self.checkRequiredConfigs()

    def test_hierarchies(self):
        # the final exhale.graph.ExhaleRoot object
        exhale_root = self.app.exhale_root
        # verify the file hierarchy and file declaration relationships
        f_hierarchy = file_hierarchy({
            directory("include"): {
                file("main.h"): {
                    function("void", "add"): signature("int a", "int b"),
                    function("void", "sub"): signature("int a", "int b")
                }
            }
        })
        compare_file_hierarchy(self, f_hierarchy, exhale_root)
        # # verify the class hierarchy and parental relationships
        # compare_class_hierarchy(self, {}, exhale_root)
        # verify_all_nodes_in_hierarchies()


@no_run
class CMathsTestsNoRun(ExhaleTestCase):
    """
    Secondary test case for project ``c_maths``.

    A :func:`testing.decorators.no_run` decorated test class.
    """

    test_project = "c_maths"
    """
    Index into ``testing/projects``.

    See also: :data:`testing.base.ExhaleTestCase.test_project`.
    """

    def test_classwide_no_run(self):
        """
        Verify that the default ``"./api"`` folder is indeed **not** generated.
        """
        exhale_args = self.app.config.exhale_args
        containmentFolder = exhale_args["containmentFolder"]
        self.assertEqual(containmentFolder, "./api")

        # check that nothing has been generated
        containmentFolder = self.getAbsContainmentFolder()
        self.assertFalse(os.path.exists(containmentFolder))
